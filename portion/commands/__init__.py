from typing import Dict

from portion.base import CommandBase
from .add import AddCommand
from .create import CreateCommand


def get_commands() -> Dict[str, type[CommandBase]]:
    return {
        "create": CreateCommand,
        "add": AddCommand,
    }
