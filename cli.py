import argparse
from consts import STRNULL


def cli() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog='copier',
        description='Copy your stored credentials on your pc'
    )
    parser.set_defaults(command='copy')
    parser.add_argument(
        '-c', '--credential',
        help='The credential to copy',
        default=STRNULL
    )
    subparsers = parser.add_subparsers(title='subcommands')
    config_parser = subparsers.add_parser('config', help='Manage the copier config')
    config_parser.set_defaults(command='config')
    config_parser.add_argument(
        '-k', '--key',
        help='Search by key into your config',
        required=False,
        default=STRNULL
    )

    return parser.parse_args()
