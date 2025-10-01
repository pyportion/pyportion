from typing import Dict

from portion.base import CommandBase
from .new import NewCommand
from .template import TemplateCommand


def get_commands() -> Dict[str, type[CommandBase]]:
    return {
        "new": NewCommand,
        "template": TemplateCommand,
    }
