from commands.subcommand import Subcommand, V
from typing import Dict
from formatter import Formatter
from rc import RcManager


class Config(Subcommand):
    def meta(self, args):
        self.rc_manager = RcManager()
        self.config = self.rc_manager.parse()
        self.formatter = Formatter()

    def main(self, args: Dict[str, V]) -> int:
        self.meta(args)
        self.formatter.set_dct(self.config)
        self.formatter.format_and_print()
        return 0