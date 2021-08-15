import pyperclip
from cli import cli
from rc import RcManager
from log import error, success, info


class App:
    def __init__(self):
        self.args = cli()
        self.rc_manager = RcManager()
        self.config = self.rc_manager.parse()

    def copy_credential(self, credential: str):
        info(f'Copying "{credential}" to your clipboard...')
        pyperclip.copy(credential)
        success('Copied successfully to your clipboard, try using Ctrl-Shift-v')


    def main(self):
        if not self.args.credential in self.config['credentials']:
            error(f'"{self.args.credential}" does not exists in your credentials')
        self.copy_credential(self.config['credentials'][self.args.credential])


if __name__ == '__main__':
    app = App()
    app.main()