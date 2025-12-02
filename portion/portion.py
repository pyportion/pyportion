import typer

from portion.handler import load_handlers
from portion.models import cli_state


class Portion:
    def __init__(self) -> None:
        self.cli = typer.Typer(callback=self.callback,
                               add_completion=True,
                               help="Portion CLI - Scaffolding Tool")

    def callback(self,
                 verbose: bool = typer.Option(
                     False,
                     "--verbose", "-v",
                     help="Enable verbose mode")) -> None:
        cli_state.verbose = verbose

    def run(self) -> None:
        load_handlers(self.cli)
        self.cli()
