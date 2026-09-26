from dataclasses import dataclass


@dataclass
class DebloatAction:
    title: str
    description: str
    risk: str = "Low"


def get_default_debloat_actions() -> list[DebloatAction]:
    return [
        DebloatAction(
            title="Disable startup apps",
            description="Reduce boot time by disabling apps you do not need immediately.",
            risk="Low",
        ),
        DebloatAction(
            title="Clear temporary files",
            description="Free up disk space from cache folders and stale temp files.",
            risk="Low",
        ),
        DebloatAction(
            title="Remove duplicate software",
            description="Uninstall duplicate or unused tools to free resources.",
            risk="Medium",
        ),
        DebloatAction(
            title="Turn off visual effects",
            description="Improve responsiveness by reducing unnecessary animations.",
            risk="Low",
        ),
        DebloatAction(
            title="Pause background sync",
            description="Stop cloud and sync tools from draining resources during focus sessions.",
            risk="Low",
        ),
    ]
