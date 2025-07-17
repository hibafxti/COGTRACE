# COGTRACE

COGTRACE is a minimalist cognitive clarity tracker built in Python. It offers a private, GUI-based logging interface for mental state self-monitoring. No background tracking, no cloud storage, and no behavioral surveillance.

This is version 0.2, the first stable prototype. It is designed to serve as a clean and expandable foundation for future cognitive-state tools.


## Overview

Presents a local slider-based GUI

Records self-rated mental clarity (0–10 scale)

Logs all entries with timestamps to a local JSON file

Built to be extended with optional analytics, exports, and additional inputs


## Installation

Requires Python 3.7 or higher.

pip install FreeSimpleGUI


## Usage

Run the script from terminal:

python cogtrace_mvp.py

Each time you submit a clarity rating, the following is appended to cogtrace_log.json:

{
"timestamp": "2025-07-17T16:32:11.123Z",
"clarity": 7
}


## File Structure

cogtrace_mvp.py — Main GUI script

cogtrace_log.json — Data log of clarity ratings

requirements.txt — Dependency list for pip install


## Upcoming Additions

analyze_log.py — plots and trends over time

Additional sliders (fatigue, focus, sharpness)

Export functionality for CSV or Notion integration


## Philosophy

COGTRACE is intentionally minimal. It is built for clarity logging without disruption. No coaching, no gamification. Just one input, one timestamp, one clean record.

It is quietly designed for individuals who want control over their cognitive data without friction.

This project is vibe-coded and extendable. It will remain lightweight by default.
