from dataclasses import dataclass, field


@dataclass
class FocusSettings:
    enabled: bool = False
    duration_minutes: int = 25
    blocked_apps: list[str] = field(
        default_factory=lambda: [
            "Discord",
            "Steam",
            "Spotify",
            "Slack",
            "YouTube",
            "Twitter",
        ]
    )


class FocusManager:
    def __init__(self):
        self.settings = FocusSettings()

    def toggle(self, enabled: bool):
        self.settings.enabled = enabled
        return enabled

    def set_duration(self, minutes: int):
        self.settings.duration_minutes = minutes

    def get_status_text(self) -> str:
        if self.settings.enabled:
            return f"Focus Mode is active for {self.settings.duration_minutes} minutes."
        return "Focus Mode is off."
