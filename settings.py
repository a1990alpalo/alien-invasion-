from pathlib import Path


class Settings:
    """Store settings for Alien Invasion."""

    def __init__(self) -> None:
        self.name = "Alien Invasion"
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60
        self.bg_file = (
            Path.cwd()
            / "Assets"
            / "images"
            / "Starbasesnow.png"
        )