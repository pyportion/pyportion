from typer import Typer

from .init import InitHandler
from .new import NewHandler
from .template import TemplateHandler
from .version import VersionHandler


def load_handlers(app: Typer) -> None:
    all_commands = [
        InitHandler,
        TemplateHandler,
        NewHandler,
        VersionHandler
    ]

    for command in all_commands:
        command(app)
