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
                     help="Enable verbose mode"),
                 auto_confirm: bool = typer.Option(
                     False,
                     "--yes", "-y",
                     help="Auto Confirm"),
                 ) -> None:
        cli_state.verbose = verbose
        cli_state.auto_confirm = auto_confirm

    def run(self) -> None:
        load_handlers(self.cli)
        self.cli()
