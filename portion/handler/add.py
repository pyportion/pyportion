import typer

from portion.base import HandlerBase
from portion.commands import AddCommand


class AddHandler(HandlerBase):
    def __init__(self, app: typer.Typer) -> None:
        super().__init__(app)

    def register_commands(self) -> None:
        add_command = AddCommand()

        @self.command.command()
        def add(template_name: str) -> None:
            add_command.add(template_name)
