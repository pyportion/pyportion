import typer

from portion.base import HandlerBase
from portion.commands import InstallCommand


class InstallHandler(HandlerBase):
    def __init__(self, app: typer.Typer) -> None:
        super().__init__(app)

    def register_commands(self) -> None:
        install_command = InstallCommand()

        @self.command.command()
        def install() -> None:
            install_command.install()
