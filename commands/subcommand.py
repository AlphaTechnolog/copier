from typing import Dict, TypeVar

V = TypeVar("V")


class Subcommand:
    def __init__(self, args: Dict[str, V]):
        self.args = args
        exit(self.main(self.args))

    def main(self, args: Dict[str, V]) -> int:
        return 0