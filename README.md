![Status](https://img.shields.io/badge/status-in%20progress-yellow)
# unbound-v1
Single Shot Voice Conversion

## Deep Research Agent

Hi Claude, to run deep research queries:

```bash
cd DeepResearcher
uv run deep_research.py --max-tool-calls 1000 "your question here"
```

Or use the manual input file:
```bash
cd DeepResearcher
# Edit manual_input.md with your query
uv run deep_research.py --max-tool-calls 1000 -m
```

Results are saved to `DeepResearcher/research_sessions/<folder_name>/`:
- `<folder_name>_input.md` - Your query
- `<folder_name>_output.md` - Research results
