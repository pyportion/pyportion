import typer

from portion.base import HandlerBase
from portion.commands import NewCommand


class NewHandler(HandlerBase):
    def __init__(self, app: typer.Typer) -> None:
        super().__init__(app)

    def register_commands(self) -> None:
        new_command = NewCommand()

        @self.command.command()
        def new(template_name: str, project_name) -> None:
            new_command.new(template_name, project_name)
