from sys import stderr
from colorama import init, Fore

init(autoreset=True)


def error(message: str):
    print(Fore.RED + message + Fore.RESET, file=stderr)
    exit(1)


def success(message: str):
    print(Fore.GREEN + message + Fore.RESET)


def warning(message: str):
    print(Fore.YELLOW + message + Fore.RESET, file=stderr)


def info(message: str):
    print(Fore.BLUE + message + Fore.RESET)
