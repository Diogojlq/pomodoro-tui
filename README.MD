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
### How to change preset timers

If you want to change the preset timers, you can do so by changing the values on:
```
class TimeSelector(Static):
    def compose(self) -> ComposeResult:
        yield Grid(
             Button("25 Min", id="btn-25"), << Change the first parameter here
             Button("30 Min", id="btn-30"), <<
             Button("45 Min", id="btn-45"), <<
             id="time-selector")
```
* And here

class MenuScreen(Screen):
    def compose(self) -> ComposeResult:
        with Container():
            yield TimeSelector()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        times = {
            "btn-25": 25 * 60,
            "btn-30": 30 * 60,
            "btn-45": 45 * 60
        }
