from portion.base import CommandBase


class AddCommand(CommandBase):
    def __init__(self, key=None) -> None:
        print(key)

    def execute(self) -> None:
        print("here")
