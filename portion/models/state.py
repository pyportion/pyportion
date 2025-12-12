from dataclasses import dataclass


@dataclass
class State:
    auto_confirm = False
    verbose: bool = False


cli_state = State()
