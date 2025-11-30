from textual.app import App, ComposeResult
from textual.widgets import Static, Button, Header, Footer
from textual.containers import Container
from textual.screen import Screen

class TimerDisplay(Static):
    def __init__(self, total_seconds):
        super().__init__()
        self.total_seconds = total_seconds
        self.timer_interval = None

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
        self.update(f"{minutes:02d}:{seconds:02d}")

class TimeSelector(Static):
    def compose(self) -> ComposeResult:
        yield Static("Select Focus Duration", classes="title")
        with Container(classes="buttons-container"):
            yield Button("25 Min", id="btn-25", variant="success")
            yield Button("30 Min", id="btn-30", variant="warning")
            yield Button("45 Min", id="btn-45", variant="error")

class TimerScreen(Screen):
    def __init__(self, seconds):
        super().__init__()
        self.seconds = seconds

    def compose(self) -> ComposeResult:
        yield Header()
        with Container(id="box"):
            yield TimerDisplay(self.seconds)
            yield Button("Cancel", id="btn-back", variant="default")
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "btn-back":
            self.dismiss()

class TimerApp(App):
    def compose(self) -> ComposeResult:
        yield TimerDisplay()

if __name__ == "__main__":
    TimerApp().run()
