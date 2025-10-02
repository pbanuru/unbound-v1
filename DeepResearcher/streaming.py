"""Streaming research with rich UI and progress tracking."""

import time
from datetime import datetime, timedelta
from rich.console import Console
from rich.live import Live
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TimeElapsedColumn
from rich.table import Table
from rich.text import Text


class ResearchTracker:
    """Track research progress and display updates."""

    def __init__(self, max_tool_calls, model):
        self.console = Console()
        self.max_tool_calls = max_tool_calls
        self.model = model
        self.start_time = time.time()
        self.tool_calls = 0
        self.web_searches = 0
        self.code_calls = 0
        self.mcp_calls = 0
        self.file_searches = 0
        self.recent_actions = []
        self.max_recent = 5

    def get_elapsed_time(self):
        """Get elapsed time as formatted string."""
        elapsed = time.time() - self.start_time
        return str(timedelta(seconds=int(elapsed)))

    def get_progress_percent(self):
        """Get completion percentage."""
        if self.max_tool_calls == 0:
            return 0.0
        return min(100.0, (self.tool_calls / self.max_tool_calls) * 100)

    def get_eta(self):
        """Calculate ETA for completion."""
        if self.tool_calls == 0:
            return "Calculating...", "Calculating..."

        elapsed = time.time() - self.start_time
        rate = self.tool_calls / elapsed  # tool calls per second
        remaining_calls = self.max_tool_calls - self.tool_calls

        if remaining_calls <= 0 or rate == 0:
            return "0 min", datetime.now().strftime("%H:%M:%S")

        remaining_seconds = remaining_calls / rate
        eta_time = datetime.now() + timedelta(seconds=remaining_seconds)

        # Format remaining time
        remaining_minutes = int(remaining_seconds / 60)
        if remaining_minutes == 0:
            remaining_str = "< 1 min"
        else:
            remaining_str = f"{remaining_minutes} min"

        return remaining_str, eta_time.strftime("%I:%M:%S %p")

    def add_action(self, action_type, description):
        """Add a recent action to the tracker."""
        self.recent_actions.append({
            "type": action_type,
            "desc": description,
            "time": datetime.now().strftime("%I:%M:%S %p")
        })
        if len(self.recent_actions) > self.max_recent:
            self.recent_actions.pop(0)

    def increment_tool_call(self, call_type):
        """Increment tool call counters."""
        self.tool_calls += 1
        if call_type == "web_search_call":
            self.web_searches += 1
        elif call_type == "code_interpreter_call":
            self.code_calls += 1
        elif call_type == "mcp_tool_call":
            self.mcp_calls += 1
        elif call_type == "file_search_call":
            self.file_searches += 1

    def create_display(self):
        """Create the rich display panel."""
        # Progress bar
        progress_percent = self.get_progress_percent()
        remaining_time, eta_time = self.get_eta()

        # Stats table
        stats = Table.grid(padding=(0, 2))
        stats.add_column(style="cyan", justify="right")
        stats.add_column(style="white")

        stats.add_row("Model:", self.model)
        stats.add_row("Elapsed:", self.get_elapsed_time())
        stats.add_row("Progress:", f"{progress_percent:.1f}% ({self.tool_calls}/{self.max_tool_calls} calls)")
        stats.add_row("ETA:", f"{remaining_time} (finishes ~{eta_time})")
        stats.add_row("", "")
        stats.add_row("Web Searches:", str(self.web_searches))
        if self.code_calls > 0:
            stats.add_row("Code Calls:", str(self.code_calls))
        if self.mcp_calls > 0:
            stats.add_row("MCP Calls:", str(self.mcp_calls))
        if self.file_searches > 0:
            stats.add_row("File Searches:", str(self.file_searches))

        # Recent actions
        if self.recent_actions:
            stats.add_row("", "")
            stats.add_row("Recent Actions:", "")
            for action in self.recent_actions[-5:]:
                action_text = Text()
                action_text.append(f"[{action['time']}] ", style="dim")
                action_text.append(action['desc'], style="yellow")
                stats.add_row("", action_text)

        # Progress bar
        bar_width = 40
        filled = int((progress_percent / 100) * bar_width)
        bar = "█" * filled + "░" * (bar_width - filled)
        progress_text = f"\n[cyan]{bar}[/cyan] {progress_percent:.1f}%"

        return Panel(
            Text.from_markup(f"{stats}\n{progress_text}"),
            title="[bold green]Deep Research Progress[/bold green]",
            border_style="green"
        )


def stream_research(client, request_params, tracker):
    """Stream research with live progress updates."""
    console = Console()

    # Start streaming
    stream = client.responses.create(**request_params, stream=True)

    events = []
    final_response = None

    with Live(tracker.create_display(), console=console, refresh_per_second=4) as live:
        for event in stream:
            events.append(event)

            # Handle different event types
            event_type = getattr(event, 'type', None)

            if event_type == 'response.created':
                tracker.add_action("system", "Research started")

            elif event_type == 'response.output_item.added':
                item = getattr(event, 'item', None)
                if item:
                    item_type = getattr(item, 'type', None)
                    if item_type in ['web_search_call', 'code_interpreter_call', 'mcp_tool_call', 'file_search_call']:
                        tracker.increment_tool_call(item_type)

                        # Get action details
                        if item_type == 'web_search_call' and hasattr(item, 'action'):
                            action = item.action
                            action_type = getattr(action, 'type', 'unknown')
                            if action_type == 'search':
                                query = getattr(action, 'query', '')[:50]
                                tracker.add_action("web", f"Searching: {query}")
                            elif action_type == 'open_page':
                                url = getattr(action, 'url', '')[:50]
                                tracker.add_action("web", f"Opening: {url}")
                            elif action_type == 'find_in_page':
                                query = getattr(action, 'query', '')[:50]
                                tracker.add_action("web", f"Finding: {query}")

                        elif item_type == 'code_interpreter_call':
                            tracker.add_action("code", "Executing code")

                        elif item_type == 'mcp_tool_call':
                            tracker.add_action("mcp", "MCP tool call")

                        elif item_type == 'file_search_call':
                            tracker.add_action("file", "Searching files")

            elif event_type == 'response.done':
                final_response = getattr(event, 'response', None)
                tracker.add_action("system", "Research complete!")

            # Update display
            live.update(tracker.create_display())

    return final_response, events
