import typer

from portion.base import HandlerBase
from portion.commands import InitCommand


class InitHandler(HandlerBase):
    def __init__(self, app: typer.Typer) -> None:
        super().__init__(app)

    def register_commands(self) -> None:
        init_command = InitCommand()

        @self.command.command()
        def init(project_name: str) -> None:
            init_command.init(project_name)
