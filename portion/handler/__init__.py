from typer import Typer

from .init import InitHandler
from .new import NewHandler
from .template import TemplateHandler
from .version import VersionHandler
from .manage import ManageHandler


def load_handlers(app: Typer) -> None:
    all_commands = [
        InitHandler,
        TemplateHandler,
        NewHandler,
        VersionHandler,
        ManageHandler,
    ]

    for command in all_commands:
        command(app)
