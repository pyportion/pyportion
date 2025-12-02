from __future__ import annotations

from rich.console import Console
from rich.theme import Theme

from portion.models import cli_state


class Logger:
    def __new__(cls) -> Logger:
        if not hasattr(cls, "_instance"):
            cls._instance = super(cls, Logger).__new__(cls)
        return cls._instance

    def __init__(self) -> None:

        theme = Theme({
            "info": "white",
            "warn": "yellow",
            "error": "red",
        })
        self.console = Console(theme=theme)

    def pulse(self, message: str, **kwargs: str) -> None:
        if cli_state.verbose:
            self.console.log(message.format(**kwargs))

    def info(self, message: str, **kwargs: str) -> None:
        message = message.format(**kwargs)
        self.console.print(f"[info]{message}[/info]")

    def warn(self, message: str, **kwargs: str) -> None:
        message = message.format(**kwargs)
        self.console.print(f"[warn]{message}[/warn]")

    def error(self, message: str, **kwargs: str) -> None:
        message = message.format(**kwargs)
        self.console.print(f"[error]Error: {message}[/error]")
