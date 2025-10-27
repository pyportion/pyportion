from typer import Typer

from .init import InitHandler
from .new import NewHandler
from .template import TemplateHandler


def load_handlers(app: Typer) -> None:
    all_commands = [
        InitHandler,
        TemplateHandler,
        NewHandler
    ]

    for command in all_commands:
        command(app)
