import os

class VideoInput:
    ALLOWED_EXTENSIONS = (".mp4", ".mov", ".mkv", ".webm")

    def __init__(self, path: str):
        self.path = path
        self._validate()

    def _validate(self):
        # Check file exists
        if not os.path.isfile(self.path):
            raise FileNotFoundError(f"Video file not found: {self.path}")

        # Check extension
        if not self.path.lower().endswith(self.ALLOWED_EXTENSIONS):
            raise TypeError(
                f"Unsupported file type. Allowed: {', '.join(self.ALLOWED_EXTENSIONS)}"
            )

    def __repr__(self):
        return f"<VideoInput path={self.path}>"



