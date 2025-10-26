from typer import Typer

from .new import NewController
from .template import TemplateController


def load_commands(app: Typer) -> None:
    all_commands = [
        TemplateController,
        NewController
    ]

    for command in all_commands:
        command(app)
