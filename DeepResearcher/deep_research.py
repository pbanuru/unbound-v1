#!/usr/bin/env python3
"""
Deep Research CLI Tool
Uses OpenAI's deep research models to conduct comprehensive research on user queries.
"""

import argparse
import json
import os
import re
import sys
import time
from datetime import datetime
from pathlib import Path
from openai import OpenAI


def generate_folder_name(client, query):
    """Generate a concise folder name based on the query using GPT."""
    try:
        response = client.responses.create(
            model="gpt-5-mini",
            reasoning={"effort": "low"},
            input=f"Generate a short, descriptive folder name (2-4 words, snake_case) for this research query: '{query}'. Only return the folder name, nothing else.",
        )
        folder_name = response.output_text.strip().lower()
        # Clean up the folder name
        folder_name = re.sub(r'[^\w\s-]', '', folder_name)
        folder_name = re.sub(r'[-\s]+', '_', folder_name)
        return folder_name
    except Exception as e:
        # Fallback to a simple truncated version
        fallback = re.sub(r'[^\w\s-]', '', query.lower())[:40]
        fallback = re.sub(r'[-\s]+', '_', fallback)
        return fallback


def create_research_folder(base_dir, folder_name):
    """Create a unique research folder with disambiguation code if needed."""
    base_path = Path(base_dir) / folder_name

    # If folder doesn't exist, create it
    if not base_path.exists():
        base_path.mkdir(parents=True, exist_ok=True)
        return base_path

    # If it exists, add disambiguation code
    counter = 1
    while True:
        disambiguated_path = Path(base_dir) / f"{folder_name}_{counter:03d}"
        if not disambiguated_path.exists():
            disambiguated_path.mkdir(parents=True, exist_ok=True)
            return disambiguated_path
        counter += 1


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


def main():
    parser = argparse.ArgumentParser(
        description="Conduct deep research using OpenAI's deep research models"
    )
    parser.add_argument(
        "query",
        nargs="?",
        help="Research query to investigate"
    )
    parser.add_argument(
        "--model",
        default="o4-mini-deep-research",
        choices=["o3-deep-research", "o4-mini-deep-research"],
        help="Model to use for research (default: o4-mini-deep-research)"
    )
    parser.add_argument(
        "--no-background",
        action="store_true",
        help="Run research synchronously (default: background mode)"
    )
    parser.add_argument(
        "--max-tool-calls",
        type=int,
        default=100,
        help="Maximum number of tool calls to make (default: 100)"
    )
    parser.add_argument(
        "--no-web-search",
        action="store_true",
        help="Disable web search"
    )
    parser.add_argument(
        "--code-interpreter",
        action="store_true",
        help="Enable code interpreter for data analysis"
    )
    parser.add_argument(
        "--interactive",
        action="store_true",
        help="Enter interactive mode for multi-line queries"
    )
    parser.add_argument(
        "--input-file",
        type=str,
        help="Read query from a markdown file"
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="./research_sessions",
        help="Directory to save research sessions (default: ./research_sessions)"
    )
    parser.add_argument(
        "--no-save",
        action="store_true",
        help="Don't save research session to disk"
    )

    args = parser.parse_args()

    # Get API key from environment
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY environment variable not set", file=sys.stderr)
        sys.exit(1)

    # Get query from various sources
    query = None
    query_source = "cli"

    if args.input_file:
        # Read from markdown file
        try:
            with open(args.input_file, "r") as f:
                query = f.read().strip()
            query_source = f"file:{args.input_file}"
            print(f"Loaded query from {args.input_file}")
        except Exception as e:
            print(f"Error reading input file: {e}", file=sys.stderr)
            sys.exit(1)
    elif args.interactive:
        # Interactive mode
        print("Enter your research query (press Ctrl+D when done):")
        query = sys.stdin.read().strip()
        query_source = "interactive"
    elif args.query:
        # Command line argument
        query = args.query
        query_source = "cli"
    else:
        # No query provided
        print("Error: No query provided. Use a query argument, --input-file, or --interactive", file=sys.stderr)
        sys.exit(1)

    if not query:
        print("Error: Query is empty", file=sys.stderr)
        sys.exit(1)

    # Initialize client
    client = OpenAI(api_key=api_key, timeout=3600)

    # Generate folder structure if saving
    research_folder = None
    if not args.no_save:
        print("Generating folder name...")
        folder_name = generate_folder_name(client, query)
        research_folder = create_research_folder(args.output_dir, folder_name)
        print(f"Research will be saved to: {research_folder}")

    # Build tools list
    tools = []
    if not args.no_web_search:
        tools.append({"type": "web_search_preview"})
    if args.code_interpreter:
        tools.append({"type": "code_interpreter", "container": {"type": "auto"}})

    if not tools:
        print("Error: At least one tool must be enabled", file=sys.stderr)
        sys.exit(1)

    # Build request parameters
    request_params = {
        "model": args.model,
        "input": query,
        "background": not args.no_background,
        "tools": tools,
        "max_tool_calls": args.max_tool_calls,
    }

    print(f"Starting research with {args.model}...")
    print(f"Query: {query}\n")

    # Create research request
    try:
        response = client.responses.create(**request_params)

        # Handle background mode
        if not args.no_background:
            print(f"Research started in background (ID: {response.id})")
            print("Polling for completion...")

            while response.status in {"queued", "in_progress"}:
                print(f"Status: {response.status}")
                time.sleep(5)
                response = client.responses.retrieve(response.id)

            print(f"\nFinal status: {response.status}\n")

        # Output results
        if response.status == "completed":
            print("=" * 80)
            print("RESEARCH RESULTS")
            print("=" * 80)
            print()
            print(response.output_text)
            print()

            # Show tool usage summary
            if hasattr(response, 'output') and response.output:
                web_searches = sum(1 for item in response.output if item.get('type') == 'web_search_call')
                code_calls = sum(1 for item in response.output if item.get('type') == 'code_interpreter_call')

                print("=" * 80)
                print("TOOL USAGE SUMMARY")
                print("=" * 80)
                if web_searches:
                    print(f"Web searches: {web_searches}")
                if code_calls:
                    print(f"Code interpreter calls: {code_calls}")

            # Save research session
            if research_folder:
                print()
                print("=" * 80)
                print("SAVING RESEARCH SESSION")
                print("=" * 80)
                input_file, output_file, metadata_file = save_research_session(
                    research_folder, query, response, args, query_source
                )
                print(f"Input saved to:    {input_file}")
                print(f"Output saved to:   {output_file}")
                print(f"Metadata saved to: {metadata_file}")
        else:
            print(f"Error: Research failed with status: {response.status}", file=sys.stderr)
            sys.exit(1)

    except KeyboardInterrupt:
        print("\nResearch interrupted by user", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
