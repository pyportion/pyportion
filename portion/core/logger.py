import time
import logging


logging.basicConfig(level=logging.INFO, format="%(message)s")


class Logger:
    def __init__(self) -> None:
        self._quiet = False
        self._verbose = False
        self._start_time = time.monotonic()
        self._end_time = time.monotonic()

    def suppress(self) -> None:
        self._quiet = True

    def verbose(self) -> None:
        self._verbose = True

    def pulse(self, message: str) -> None:
        if not self._quiet and self._verbose:
            self._end_time = time.monotonic()
            taken_time = self._end_time - self._start_time
            logging.info(f"[Time Taken: {taken_time:.2f}s] {message}")

    def info(self, message: str) -> None:
        if not self._quiet:
            logging.info(message)
