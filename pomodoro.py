from textual.app import App, ComposeResult
from textual.widgets import Static, Button
from textual.containers import Container, Grid
from textual.screen import Screen
import pyfiglet

class TimerDisplay(Static):
    def __init__(self, total_seconds):
        super().__init__()
        self.total_seconds = total_seconds
        self.timer_interval = None
        self.figlet_font = "banner3-D"

    def on_mount(self):
        self.update_timer()
        self.timer_interval = self.set_interval(1, self.tick)

    def tick(self):
        self.total_seconds -= 1
        if self.total_seconds <= 0:
            self.update("Time's Up!")
            if self.timer_interval:
                self.timer_interval.stop()
        else:
            self.update_timer()

    def update_timer(self):
        minutes, seconds = divmod(self.total_seconds, 60)
        time_string = f"{minutes:02d}:{seconds:02d}"
        
        ascii_art = pyfiglet.figlet_format(
            time_string, 
            font=self.figlet_font
        )
        
        self.update(ascii_art)

class TimeSelector(Static):
    def compose(self) -> ComposeResult:
        yield Grid(
             Button("25 Min", id="btn-25"),
             Button("30 Min", id="btn-30"),
             Button("45 Min", id="btn-45"),
             id="time-selector")

class TimerScreen(Screen): # when playing the timer
    def __init__(self, seconds):
        super().__init__()
        self.seconds = seconds

    def compose(self) -> ComposeResult:
        yield Grid(
            TimerDisplay(self.seconds)
            )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "btn-back":
            self.dismiss()

class MenuScreen(Screen):
    def compose(self) -> ComposeResult:
        with Grid(id="main-grid"):
            yield TimeSelector()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        times = {
            "btn-25": 25 * 60,
            "btn-30": 30 * 60,
            "btn-45": 45 * 60
        }
        selected_time = times.get(event.button.id)
        
        if selected_time:
            self.app.push_screen(TimerScreen(selected_time))

class PomodoroApp(App):
    CSS_PATH = "style.css"      

    def on_mount(self) -> None:
        self.push_screen(MenuScreen())

if __name__ == "__main__":
    PomodoroApp().run()
