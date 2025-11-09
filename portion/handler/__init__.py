from typer import Typer

from .add import AddHandler
from .init import InitHandler
from .new import NewHandler
from .remove import RemoveHandler
from .template import TemplateHandler
from .version import VersionHandler


def load_handlers(app: Typer) -> None:
    all_commands = [
        InitHandler,
        TemplateHandler,
        NewHandler,
        VersionHandler,
        AddHandler,
        RemoveHandler,
    ]

    for command in all_commands:
        command(app)
