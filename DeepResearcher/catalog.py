"""Research session cataloging functions."""

import json
from datetime import datetime


def save_research_session(folder_path, query, response, args, query_source="cli"):
    """Save the research session data to files."""
    timestamp = datetime.now().isoformat()

    # Save input query
    input_file = folder_path / "input.md"
    with open(input_file, "w") as f:
        f.write(f"# Research Query\n\n")
        f.write(f"**Timestamp:** {timestamp}\n\n")
        f.write(f"**Source:** {query_source}\n\n")
        f.write(f"**Model:** {args.model}\n\n")
        f.write(f"**Max Tool Calls:** {args.max_tool_calls}\n\n")
        f.write(f"## Query\n\n{query}\n")

    # Save output results
    output_file = folder_path / "output.md"
    with open(output_file, "w") as f:
        f.write(f"# Research Results\n\n")
        f.write(f"**Timestamp:** {timestamp}\n\n")
        f.write(f"**Response ID:** {response.id}\n\n")
        f.write(f"**Status:** {response.status}\n\n")
        f.write(f"## Results\n\n{response.output_text}\n")

    # Save metadata and tool usage
    metadata = {
        "timestamp": timestamp,
        "query": query,
        "query_source": query_source,
        "model": args.model,
        "response_id": response.id,
        "status": response.status,
        "max_tool_calls": args.max_tool_calls,
        "web_search_enabled": not args.no_web_search,
        "code_interpreter_enabled": args.code_interpreter,
        "background_mode": not args.no_background,
    }

    # Add tool usage statistics
    if hasattr(response, 'output') and response.output:
        web_searches = sum(1 for item in response.output if item.get('type') == 'web_search_call')
        code_calls = sum(1 for item in response.output if item.get('type') == 'code_interpreter_call')
        metadata["tool_usage"] = {
            "web_searches": web_searches,
            "code_interpreter_calls": code_calls,
        }

    metadata_file = folder_path / "metadata.json"
    with open(metadata_file, "w") as f:
        json.dump(metadata, f, indent=2)

    return input_file, output_file, metadata_file
