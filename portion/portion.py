from typing import Any
from typing import List
from typing import Tuple

from portion.commands import get_commands
from portion.core import Logger
from portion.core import Parser


class Portion:
    def __init__(self) -> None:
        parser = Parser()
        self.args = parser.parse()
        self.commands = get_commands()
        self.logger = Logger(self.args.q)

    def _get_arguments(self) -> List[Tuple[Any, Any]]:
        arguments = []
        for name, value in vars(self.args).items():
            name = name.replace("-", "_")
            arguments.append((name, value))
        return arguments

    def _run_command(self) -> None:
        command = self.commands.get(self.args.command, None)
        if command:
            params = command.__init__.__code__.co_varnames[1:]
            arguments = self._get_arguments()
            kwargs = {k: v for k, v in arguments if k in params}
            command(logger=self.logger, **kwargs).execute()

    def run(self) -> None:
        self._run_command()
