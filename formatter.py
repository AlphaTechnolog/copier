from typing import Dict, TypeVar
from colorama import init, Fore

init(autoreset=True)

V = TypeVar("V")


class FormatterError(BaseException):
    pass


class Formatter:
    def __init__(self, dct: Dict[str, V] or None = None):
        self.dct = dct

    def set_dct(self, dct: Dict[str, V]):
        self.dct = dct

    def get_dct(self) -> Dict[str, V]:
        return self.dct

    def _validate__required_dct(self) -> bool:
        return self.dct is None

    def _format_list(self, lst: list, indent: int = 0):
        for val in lst:
            if (not isinstance(val, list) and
                    not isinstance(val, dict)):
                print("  " * indent + Fore.GREEN + val + Fore.RESET)
            elif isinstance(val, list):
                self._format_list(val, indent + 1)
            elif isinstance(val, dict):
                print("  " * indent + Fore.BLUE + "---------------" + Fore.RESET)
                self.format_and_print(val, indent + 1)
            else:
                raise FormatterError(f'Unsupported type {type(val)}')

    def format_and_print(self, dct: dict or None = None, indent: int = 0) -> str:
        if dct is None:
            dct = self.dct

        if dct is None:
            raise FormatterError('Invalid dictionary to format.')

        for key, val in dct.items():
            if (not isinstance(val, dict) and
                    not isinstance(val, list)):
                print("  " * indent + (Fore.YELLOW + key + Fore.RESET + ': ' + Fore.GREEN + str(val) + Fore.RESET))
            elif isinstance(val, list):
                print("  " * indent + Fore.YELLOW + key + Fore.RESET + ':')
                self._format_list(val, indent + 1)
            elif isinstance(val, dict):
                print("  " * indent + Fore.YELLOW + key + Fore.RESET + ':')
                self.format_and_print(val, indent + 1)
            else:
                raise FormatterError(f'Unsupported type for "{key}": {type(val)}')