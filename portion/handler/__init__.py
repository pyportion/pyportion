from typer import Typer

from .add import AddHandler
from .init import InitHandler
from .install import InstallHandler
from .new import NewHandler
from .remove import RemoveHandler
from .template import TemplateHandler
from .version import VersionHandler


def load_handlers(app: Typer) -> None:
    all_commands = [
        AddHandler,
        InitHandler,
        InstallHandler,
        NewHandler,
        RemoveHandler,
        TemplateHandler,
        VersionHandler,
    ]

    for command in all_commands:
        command(app)
