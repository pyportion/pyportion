
import argparse


class Parsers:
    def __init__(self, parser: argparse._SubParsersAction) -> None:
        self.command_parser = parser

    def add_commands(self) -> None:
        ...
