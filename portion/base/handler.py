from typer import Typer


class HandlerBase:
    def __init__(self, app: Typer, command: str | None = None) -> None:
        self.command = Typer(name=command)
        app.add_typer(self.command)
        self.register_commands()

    def register_commands(self) -> None:
        ...
