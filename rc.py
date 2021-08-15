import json
from paths import main as create_paths, rc_path
from typing import Dict, TypeVar

V = TypeVar("V")


class RcManager:
    def __init__(self):
        create_paths()

    def parse(self) -> Dict[str, V]:
        with open(rc_path, 'r') as configfile:
            return json.load(configfile)