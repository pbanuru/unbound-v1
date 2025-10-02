"""Debug version of streaming to inspect event structure."""

import json
import time
from datetime import datetime
from pathlib import Path


def log_event(event, log_dir="debug_logs"):
    """Log streaming events to file for inspection."""
    Path(log_dir).mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    event_type = getattr(event, 'type', 'unknown')

    # Try to use model_dump if available (Pydantic models)
    event_dict = {}
    if hasattr(event, 'model_dump'):
        try:
            event_dict = event.model_dump()
        except:
            pass

    # Fallback to manual extraction
    if not event_dict:
        for attr in dir(event):
            if not attr.startswith('_') and not callable(getattr(event, attr, None)):
                try:
                    value = getattr(event, attr)
                    event_dict[attr] = value
                except:
                    pass

    log_file = Path(log_dir) / f"{timestamp}_{event_type}.json"
    with open(log_file, 'w') as f:
        json.dump(event_dict, f, indent=2, default=str)

    return log_file


def debug_stream_research(client, request_params, tracker):
    """Stream research with full event logging for debugging."""
    from rich.console import Console
    from rich.live import Live

    console = Console()
    log_dir = f"debug_logs/session_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

    # Create the directory upfront
    Path(log_dir).mkdir(parents=True, exist_ok=True)

    console.print(f"[yellow]DEBUG MODE: Logging events to {log_dir}[/yellow]")

    # Start streaming
    stream = client.responses.create(**request_params, stream=True)

    events = []
    final_response = None
    response_id = None

    with Live(tracker.create_display(), console=console, refresh_per_second=4) as live:
        for event in stream:
            # Log every event
            log_file = log_event(event, log_dir)

            events.append(event)
            event_type = getattr(event, 'type', None)

            # Log what we're seeing
            console.print(f"[dim]Event: {event_type} -> {log_file.name}[/dim]")

            if event_type == 'response.created':
                response_id = getattr(event, 'response_id', None)
                tracker.add_action("system", "Research started")

            elif event_type == 'response.output_item.added':
                item = getattr(event, 'item', None)
                if item:
                    # Log item structure using model_dump
                    item_log = {}
                    if hasattr(item, 'model_dump'):
                        try:
                            item_log = item.model_dump()
                        except:
                            pass

                    # Fallback
                    if not item_log:
                        item_log = {
                            'type': getattr(item, 'type', None),
                            'id': getattr(item, 'id', None),
                            'has_action': hasattr(item, 'action'),
                        }

                        if hasattr(item, 'action'):
                            action = item.action
                            if hasattr(action, 'model_dump'):
                                try:
                                    item_log['action'] = action.model_dump()
                                except:
                                    item_log['action'] = {'type': getattr(action, 'type', None)}

                    item_file = Path(log_dir) / f"{log_file.stem}_item_detail.json"
                    with open(item_file, 'w') as f:
                        json.dump(item_log, f, indent=2, default=str)

                    console.print(f"[cyan]Item detail: {item_file.name}[/cyan]")

                    item_type = getattr(item, 'type', None)
                    if item_type in ['web_search_call', 'code_interpreter_call', 'mcp_tool_call', 'file_search_call']:
                        tracker.increment_tool_call(item_type)

                        if item_type == 'web_search_call':
                            if hasattr(item, 'action'):
                                action = item.action
                                action_type = getattr(action, 'type', 'unknown')
                                tracker.add_action("web", f"Action: {action_type}")
                            else:
                                tracker.add_action("web", "Web search (no action)")

            elif event_type == 'response.done':
                final_response = getattr(event, 'response', None)
                tracker.add_action("system", "Research complete!")

            live.update(tracker.create_display())

    # Save summary
    summary = {
        'response_id': response_id,
        'total_events': len(events),
        'event_types': list(set(getattr(e, 'type', 'unknown') for e in events)),
        'final_response_captured': final_response is not None,
    }

    summary_file = Path(log_dir) / "summary.json"
    with open(summary_file, 'w') as f:
        json.dump(summary, f, indent=2)

    console.print(f"\n[green]Debug logs saved to: {log_dir}[/green]")
    console.print(f"[green]Summary: {summary_file}[/green]")

    # Try to retrieve final response if needed
    if not final_response and response_id:
        try:
            final_response = client.responses.retrieve(response_id)
            tracker.add_action("system", "Retrieved final response")
        except Exception as e:
            console.print(f"[yellow]Warning: Could not retrieve final response: {e}[/yellow]")

    return final_response, events
