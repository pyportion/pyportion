from typing import Dict

from portion.base import CommandBase
from .add import AddCommand
from .create import CreateCommand
from .template import TemplateCommand


def get_commands() -> Dict[str, type[CommandBase]]:
    return {
        "create": CreateCommand,
        "add": AddCommand,
        "template": TemplateCommand,
    }
