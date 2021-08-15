from commands.subcommand import Subcommand, V
from typing import Dict
from formatter import Formatter
from rc import RcManager
from consts import STRNULL


class Config(Subcommand):
    def meta(self, args):
        self.rc_manager = RcManager()
        self.config = self.rc_manager.parse()
        self.formatter = Formatter()

    def main(self, args: Dict[str, V]) -> int:
        self.meta(args)
        dct = self.config
        if not args['key'] is STRNULL:
            dct = dict()
            dct[args['key']] = self.config['credentials'][args['key']]

        self.formatter.set_dct(dct)
        self.formatter.format_and_print()
        return 0