from commands.copy import Copy
from commands.config import Config


_registry = {
    'copy': Copy,
    'config': Config
}