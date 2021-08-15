from commands.subcommand import Subcommand, V
from typing import Dict
from rc import RcManager, V as RcValue
from log import info, success, error


class Create(Subcommand):
    def main(self, args: Dict[str, V]) -> int:
        self.rc_manager = RcManager()
        info('Generating new config...')
        self.config: Dict[str, RcValue] = self.rc_manager.parse()
        self.config['credentials'][args['key']] = args['value']
        success('Generated config successfully')
        info('Trying to dump the generated config...')
        try:
            self.rc_manager.dump(self.config)
        except Exception as err:
            error(f'Upps... an exeption was occurred (please report on an github issue), error: {err}')
        success('Dumped new config successfully!')

        return 0