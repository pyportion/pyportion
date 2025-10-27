import typer

from portion.handler import load_handlers


class Portion:
    def __init__(self) -> None:
        self.cli = typer.Typer()

    def run(self) -> None:
        load_handlers(self.cli)
        self.cli()
