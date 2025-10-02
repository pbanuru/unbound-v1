"""Research session cataloging functions."""

import json
from datetime import datetime


def save_research_session(folder_path, query, response, args, query_source="cli"):
    """Save the research session data to files."""
    timestamp = datetime.now().isoformat()

    # Get folder name for file prefixes
    folder_name = folder_path.name

    # Save input query (minimal - just the query text)
    input_file = folder_path / f"{folder_name}_input.md"
    with open(input_file, "w") as f:
        f.write(query)

    # Save output results (minimal - just the results)
    output_file = folder_path / f"{folder_name}_output.md"
    with open(output_file, "w") as f:
        f.write(response.output_text)

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
        web_searches = sum(1 for item in response.output if getattr(item, 'type', None) == 'web_search_call')
        code_calls = sum(1 for item in response.output if getattr(item, 'type', None) == 'code_interpreter_call')
        metadata["tool_usage"] = {
            "web_searches": web_searches,
            "code_interpreter_calls": code_calls,
        }

    metadata_file = folder_path / "metadata.json"
    with open(metadata_file, "w") as f:
        json.dump(metadata, f, indent=2)

    return input_file, output_file, metadata_file
