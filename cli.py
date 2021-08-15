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
    config_parser_subparsers = config_parser.add_subparsers(title='subcommands')
    config_parser_subparsers_create_parser = config_parser_subparsers.add_parser(
        'create',
        help='Create a new credential from your command line'
    )
    config_parser_subparsers_create_parser.set_defaults(command='config__create')
    config_parser_subparsers_create_parser.add_argument(
        '-k', '--key',
        help='The credential key name',
        required=True
    )
    config_parser_subparsers_create_parser.add_argument(
        '-v', '--value',
        help='The credential value',
        required=True
    )

    return parser.parse_args()
