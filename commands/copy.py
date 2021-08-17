import pyperclip
from rc import RcManager
from commands.subcommand import Subcommand, V
from typing import Dict
from log import error, success, info


class Copy(Subcommand):
    def meta(self):
        self.rc_manager = RcManager()
        self.config = self.rc_manager.parse()

    def copy_credential(self, credential: str) -> int:
        info('Copying to your clipboard...')
        pyperclip.copy(str(credential))
        success('Copied successfully to your clipboard, try using Ctrl-Shift-V on your terminal to paste it!')

    def main(self, args: Dict[str, V]) -> int:
        self.meta()
        if not self.args['credential'] in self.config['credentials']:
            error('Invalid credential suplied, it\'s not registered in your .copierrc.json')

        self.copy_credential(self.config['credentials'][args['credential']])
        return 0