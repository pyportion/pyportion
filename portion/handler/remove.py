import typer

from portion.base import HandlerBase
from portion.commands import RemoveCommand


class RemoveHandler(HandlerBase):
    def __init__(self, app: typer.Typer) -> None:
        super().__init__(app)

    def register_commands(self) -> None:
        remove_command = RemoveCommand()

        @self.command.command()
        def remove(template_name: str) -> None:
            remove_command.remove(template_name)
