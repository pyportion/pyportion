from typing import Dict
from typing import Callable

import argparse

from portion.core.logger import Logger
from portion.base import CommandBase
from portion.commands import CreateCommand
from portion.commands import AddCommand


class Portion:
    def __init__(self) -> None:
        self.logger = Logger()

    def _run_command(self, args: argparse.Namespace) -> None:
        commands: Dict[str, type[CommandBase]] = {
            "create": CreateCommand,
            "add": AddCommand
        }

        command = commands.get(args.command, None)
        if command:
            params = command.__init__.__code__.co_varnames[1:]
            kwargs = {k: v for k, v in vars(args).items() if k in params}
            command(**kwargs).execute()

    def _setup_logger(self, args: argparse.Namespace) -> None:
        if args.q:
            self.logger.suppress()

        if args.v:
            self.logger.verbose()

    def add_generic_arguments(self, suparser: argparse.ArgumentParser) -> None:
        suparser.add_argument("-q",
                              default=False,
                              help="Suppress Logging",
                              action="store_true")

        suparser.add_argument("-v",
                              default=False,
                              help="Verbose Logging",
                              action="store_true")

    def _parse(self) -> None:
        parser = argparse.ArgumentParser(description="Portion")

        subparser = parser.add_subparsers(dest="command", required=True)

        create = subparser.add_parser("create", help="Create a project")
        self.add_generic_arguments(create)

        add = subparser.add_parser("add", help="Add a portion")
        self.add_generic_arguments(add)

        args = parser.parse_args()
        self._setup_logger(args)
        self._run_command(args)

    def run(self) -> None:
        self._parse()
