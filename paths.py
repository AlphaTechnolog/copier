import json
from pathlib import Path
from os.path import expanduser
from log import error, warning


home_path = Path(expanduser('~'))
rc_path = home_path / '.copierrc.json'


def main():
    if not home_path.is_dir():
        error('Cannot get the home path')
    if not rc_path.is_file():
        rc_path.touch()
        with open(rc_path, 'w') as configfile:
            json.dump({ 'credentials': {} }, configfile)
        warning(str(rc_path.absolute()) + ' was not found, it was created')


if __name__ == '__main__':
    main()
