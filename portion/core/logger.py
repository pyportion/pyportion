import time
import logging


logging.basicConfig(level=logging.INFO, format="%(message)s")


class Logger:
    def __init__(self, quiet: bool) -> None:
        self.quiet = quiet

    def error(self, message: str) -> None:
        if not self.quiet:
            logging.info("Error: " + message)

    def info(self, message: str) -> None:
        if not self.quiet:
            logging.info(message)
