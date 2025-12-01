from portion.core import Logger


class CommandBase:
    def __init__(self, **kwargs: str) -> None:
        self.logger = Logger()
