import time
import logging


logging.basicConfig(level=logging.INFO, format="%(message)s")


class Logger:
    def __init__(self, quiet: bool, verbose: bool) -> None:
        self.quiet = quiet
        self.verbose = verbose
        self._start_time = time.monotonic()
        self._end_time = time.monotonic()

    def pulse(self, message: str) -> None:
        if not self.quiet and self.verbose:
            self._end_time = time.monotonic()
            taken_time = self._end_time - self._start_time
            logging.info(f"[Time Taken: {taken_time:.2f}s] {message}")

    def error(self, message: str) -> None:
        if not self.quiet:
            logging.info("Error: " + message)

    def info(self, message: str) -> None:
        if not self.quiet:
            logging.info(message)
