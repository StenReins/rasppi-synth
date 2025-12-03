import pygame

class AudioPlayer:
    def __init__(self, *args, path=None, bpm: int = 120):
        self.path = None
        self.bpm = int(bpm) if bpm is not None else 120
        self._loop = False

        if len(args) > 0:
            first = args[0]
            if isinstance(first, int):
                self.bpm = int(first)
            elif isinstance(first, str):
                self.path = first

        if path is not None:
            self.path = path

        self._beat_duration = 60.0 / max(1, float(self.bpm))

        pygame.mixer.init()
        pygame.mixer.music.set_volume(0.9)

    def play(self, path=None, loop: bool = False):
        if path is not None:
            self.path = path
        if not self.path:
            return

        try:
            pygame.mixer.music.load(self.path)
        except Exception as e:
            print(f"Audio load error: {e}")
            return

        self._loop = bool(loop)
        pygame.mixer.music.play(loops=-1 if loop else 0)

    def set_bpm(self, bpm: int):
        self.bpm = int(bpm)
        self._beat_duration = 60.0 / max(1, float(self.bpm))

    def get_beat_duration(self) -> float:
        return self._beat_duration

    def stop(self):
        pygame.mixer.music.stop()

    def is_playing(self) -> bool:
        return pygame.mixer.music.get_busy()

    def close(self):
        self.stop()
        pygame.mixer.quit()