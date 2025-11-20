import typer

from portion.base import HandlerBase
from portion.commands import BuildCommand


class BuildHandler(HandlerBase):
    def __init__(self, app: typer.Typer) -> None:
        super().__init__(app)

    def register_commands(self) -> None:
        build_command = BuildCommand()

        @self.command.command()
        def build(portion_name: str) -> None:
            build_command.build(portion_name)
