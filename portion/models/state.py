from dataclasses import dataclass


@dataclass
class State:
    verbose: bool = False


cli_state = State()
