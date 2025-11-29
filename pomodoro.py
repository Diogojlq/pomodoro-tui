from textual.app import App, ComposeResult
from textual.widgets import Static

class Timer(Static):
    def on_mount(self):
        self.seconds = 10
        self.update(f"⏳ {self.seconds}")
        self.set_interval(1, self.update_timer)

    def update_timer(self):
        self.seconds -= 1
        if self.seconds <= 0:
            self.update("⏱️ Tempo esgotado!")
            self.set_interval(0, lambda: None)  # Para o timer
        else:
            self.update(f"⏳ {self.seconds}")

class TimerApp(App):
    def compose(self) -> ComposeResult:
        yield Timer()

if __name__ == "__main__":
    TimerApp().run()
