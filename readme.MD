# Pomodoro TUI

This is a simple Pomodoro Timer application that runs in your terminal.

## Usage

To run the application, execute the `pomodoro.py` file:

```bash
python pomodoro.py
```

Follow the on-screen instructions to start, pause, or reset the timer.

## For devs:
### How to change timer font

You can change the numbers font by changing it on:
```
class TimerDisplay(Static):
    def __init__(self, total_seconds):
        super().__init__()
        self.total_seconds = total_seconds
        self.timer_interval = None
        self.figlet_font = "banner3-D" << Here

```
Here's a **curated list**:
```
roman
rev
larry3d
univers
rowancap
doh
colossal
charset_
broadway
banner3-D
```
