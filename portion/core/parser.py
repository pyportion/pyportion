import argparse


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

    def _create_argument(self,
                         parser: argparse._SubParsersAction
                         ) -> argparse.ArgumentParser:
        create = parser.add_parser("create", help="Create a project")
        return create

    def _add_argument(self,
                      parser: argparse._SubParsersAction
                      ) -> argparse.ArgumentParser:
        add = parser.add_parser("add", help="Add a portion")
        return add

    def parse(self) -> argparse.Namespace:
        subparser = self.parser.add_subparsers(dest="command", required=True)
        argument_parsers = [
            self._create_argument(subparser),
            self._add_argument(subparser)
        ]

        for argument_parser in argument_parsers:
            self._add_generic_arguments(argument_parser)

        return self.parser.parse_args()
