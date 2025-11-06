import typer

from portion.base import HandlerBase
from portion.commands import ManageCommand


class ManageHandler(HandlerBase):
    def __init__(self, app: typer.Typer) -> None:
        super().__init__(app)

    def register_commands(self) -> None:
        manage_command = ManageCommand()

        @self.command.command()
        def add(template_name: str) -> None:
            manage_command.add(template_name)

        @self.command.command()
        def remove(template_name: str) -> None:
            manage_command.remove(template_name)
