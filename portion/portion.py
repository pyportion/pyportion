import typer

from portion.controller import load_commands


class Portion:
    def __init__(self) -> None:
        self.cli = typer.Typer()

    def run(self) -> None:
        load_commands(self.cli)
        self.cli()
