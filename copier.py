from cli import cli
from consts import STRNULL
from log import error
from commands.registry import _registry
from commands.subcommand import Subcommand


class App:
    def __init__(self):
        self.args = vars(cli())
        self._validate_args()

    def _validate_args(self):
        if self.args['command'] == 'copy' and self.args['credential'] == STRNULL:
            error("Can't bypass credential if command is copy")

    def main(self):
        if not self.args['command'] in _registry:
            error('Invalid command suplied, it no are registered')
        Command: Subcommand = _registry[self.args['command']]
        Command(self.args)


if __name__ == '__main__':
    app = App()
    app.main()