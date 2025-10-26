import typer

from portion.commands import NewCommand


class NewController:
    def __init__(self, app: typer.Typer) -> None:
        self.command = typer.Typer()
        app.add_typer(self.command)
        self._register_commands()

    def _register_commands(self) -> None:
        new_command = NewCommand()

        @self.command.command()
        def new(template_name: str, project_name) -> None:
            new_command.new(template_name, project_name)
