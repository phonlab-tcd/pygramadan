from .verb import init_moods, init_tenses


class VP:
    def __init__(self) -> None:
        self.tenses = init_tenses()
        self.moods = init_moods