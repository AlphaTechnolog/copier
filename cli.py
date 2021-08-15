import argparse


def cli() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog='copier',
        description='Copy your stored credentials on your pc'
    )
    parser.add_argument(
        '-c', '--credential',
        help='The credential to copy',
        required=True
    )

    return parser.parse_args()
