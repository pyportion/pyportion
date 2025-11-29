import typer

from portion.core.state import cli_state
from portion.handler import load_handlers


class Portion:
    def __init__(self) -> None:
        self.cli = typer.Typer(callback=self.callback,
                               add_completion=True,
                               help="Portion CLI - Scaffolding Tool")

    def callback(self,
                 verbose: bool = typer.Option(  # noqa: B008
                     False,
                     "--verbose", "-v",
                     help="Enable verbose mode")) -> None:
        cli_state.verbose = verbose

    def run(self) -> None:
        load_handlers(self.cli)
        self.cli()
