import argparse
from argparse import ArgumentParser
from argparse import _SubParsersAction
from argparse import Namespace


class Parser:
    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser(description="Portion")

    def _add_generic_arguments(self,
                               suparser: argparse.ArgumentParser) -> None:
        suparser.add_argument("-q",
                              default=False,
                              help="Suppress Logging",
                              action="store_true")

        suparser.add_argument("-v",
                              default=False,
                              help="Verbose Logging",
                              action="store_true")

    def _new_arguments(self, parser: _SubParsersAction) -> ArgumentParser:
        new: ArgumentParser = parser.add_parser("new",
                                                help="Create a new project")
        new.add_argument("template-name", help="Template Name")
        new.add_argument("project-name", help="Project Name")
        return new

    def _template_arguments(self, parser: _SubParsersAction) -> ArgumentParser:
        template: ArgumentParser = parser.add_parser("template",
                                                     help="Manage templates")
        template_subparser = template.add_subparsers(
            dest="template_command",
            help="Allows you to manage templates")

        download_parser = template_subparser.add_parser(
            "download", help="Download a template")

        download_parser.add_argument("link")

        delete_parser = template_subparser.add_parser(
            "delete", help="Delete a template")

        delete_parser.add_argument("template-name")

        template_subparser.add_parser("list", help="List all templates")

        return template

    def parse(self) -> Namespace:
        subparser = self.parser.add_subparsers(dest="command", required=True)
        argument_parsers = [
            self._new_arguments(subparser),
            self._template_arguments(subparser),
        ]

        for argument_parser in argument_parsers:
            self._add_generic_arguments(argument_parser)

        return self.parser.parse_args()
