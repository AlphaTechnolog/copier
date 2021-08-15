from commands.copy import Copy
from commands.config import Config
from commands.config__commands.create import Create as ConfigCreate


_registry = {
    'copy': Copy,
    'config': Config,
    'config__create': ConfigCreate
}