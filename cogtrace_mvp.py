import FreeSimpleGUI as sg
import json
from datetime import datetime
import os

# Ensure the log file exists
log_file = "cogtrace_log.json"
if not os.path.exists(log_file):
    with open(log_file, "w") as f:
        json.dump([], f)

# UI layout
layout = [
    [sg.Text('How clear is your mind right now?')],
    [sg.Slider(range=(0, 10), orientation='h', key='clarity')],
    [sg.Text('Do you feel in control of your tasks?')],
    [sg.Radio('Yes', "RADIO1", key='yes'), sg.Radio('No', "RADIO1", key='no')],
    [sg.Button('Log Entry'), sg.Button('Exit')]
]

# Create the window
window = sg.Window('COGTRACE Check-In', layout)

# Event loop
while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, 'Exit'):
        break
    if event == 'Log Entry':
        entry = {
            "timestamp": datetime.now().isoformat(),
            "clarity": int(values['clarity']),
            "control": "yes" if values['yes'] else "no"
        }
        # Load existing data
        with open(log_file, "r") as f:
            data = json.load(f)
        # Append new entry
        data.append(entry)
        # Save updated data
        with open(log_file, "w") as f:
            json.dump(data, f, indent=2)
        sg.popup('Logged!', auto_close=True, auto_close_duration=1)

window.close()
