# Pomodoro TUI

This is a simple Pomodoro Timer application that runs in your terminal.

## Installation

I recommend using pipx to install this application. pipx installs Python applications into isolated environments, making them accessible system-wide without cluttering your main Python environment or the project's dependencies.

1. Get the Code (Cloning the Repository)
First, you need to clone the repository to your local machine:
```
git clone https://github.com/Diogojlq/pomodoro-tui
cd pomodoro-tui
```
2. Prerequisites: Install pipx
If you don't have pipx installed yet, you need to install it globally using pip:
```
pip install --user pipx
```
After installation, ensure that the applications installed by pipx are accessible in your system's PATH. This usually requires running:

```
python -m pipx ensurepath
```
Note: You may need to restart your terminal session (or open a new one) for the pipx command to become available after running ensurepath.

3. Install the Application:
Since you are installing from the local project directory (which you cloned in Step 1), use the following command while you are inside the your-repo-name folder:

```
pipx install .
```

4. Usage:
You can now run the application's command from any directory in your terminal:

```
pomodoro
```

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
            "btn-25": 25 * 60, << 
            "btn-30": 30 * 60, <<
            "btn-45": 45 * 60  <<
        }
```

### License

This project is licensed under the **MIT License**. See the LICENSE.md file for details.

You are free to use, modify, and distribute the code, provided that you maintain the copyright attribution and the license notice included.