
import typer

from portion.base import HandlerBase
from portion.commands import VersionCommand


class VersionHandler(HandlerBase):
    def __init__(self, app: typer.Typer) -> None:
        super().__init__(app)

    def register_commands(self) -> None:
        version_command = VersionCommand()

        @self.command.command()
        def version() -> None:
            version_command.version()
