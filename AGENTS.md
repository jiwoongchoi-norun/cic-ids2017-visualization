# Project: CIC IDS 2017 Traffic Analysis

## Goal
Analyze and visualize network attack traffic patterns using CIC IDS 2017 dataset.

## Scope
This is a Python data analysis project.
Focus on pandas preprocessing, aggregation, and visualization.

## Dataset
Use CIC IDS 2017 CSV files.
Start with one CSV file first, not all.

## Folder Rules
- data/raw/: original CSV (do not modify)
- data/processed/: cleaned data
- data/sample/: small sample for testing
- notebooks/: experiments only
- src/: main code

## Coding Rules
- Keep code simple and readable
- Use pandas mainly
- Add Korean comments
- Do not over-engineer
- Work step by step

## Analysis Targets
1. Normal vs attack ratio
2. Attack type distribution
3. Port distribution
4. Flow duration stats

## Done Criteria
- Explain changed files
- Show how to run code
- Keep output clear

## MCP Usage
- Use Context7 only when library usage or API behavior is unclear.
- Prefer local code and current project files first.
- Do not call MCP for simple pandas/matplotlib code unless needed.
- If using Context7, summarize only the relevant part briefly.

For Codex workflow rules, refer to docs/codex_workflow.md.