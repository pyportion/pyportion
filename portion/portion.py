from portion.core.parser import Parser
from portion.core.logger import Logger
from portion.commands import get_commands


class Portion:
    def __init__(self) -> None:
        parser = Parser()
        self.args = parser.parse()
        self.commands = get_commands()
        self.logger = Logger(self.args.q, self.args.v)

    def _run_command(self) -> None:
        command = self.commands.get(self.args.command, None)
        if command:
            params = command.__init__.__code__.co_varnames[1:]
            kwargs = {k: v for k, v in vars(self.args).items() if k in params}
            command(self.logger, **kwargs).execute()

    def run(self) -> None:
        self._run_command()
