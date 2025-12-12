from typer import Typer

from .add import AddHandler
from .build import BuildHandler
from .info import InfoHandler
from .init import InitHandler
from .install import InstallHandler
from .new import NewHandler
from .remove import RemoveHandler
from .template import TemplateHandler
from .version import VersionHandler


def load_handlers(app: Typer) -> None:
    all_commands = [
        AddHandler,
        BuildHandler,
        InfoHandler,
        InitHandler,
        InstallHandler,
        NewHandler,
        RemoveHandler,
        TemplateHandler,
        VersionHandler,
    ]

    for command in all_commands:
        command(app)
