import os
from typing import Literal, Optional, Tuple, TypeAlias, TypeVar
from pathlib import Path
import toml

SYSTEM = Literal["Windows", "Darwin", "Linux"]


def find_config_file(system: SYSTEM) -> str:
    home_path: Path = Path.home()
    match system:
        case "Windows":
            pass
        case "Linux":
            pass
        case "Darwin":
            try:
                data = toml.load(
                    str(home_path) + "/Library/Application Support/Anki2/test.toml"
                )
            except FileNotFoundError:
                print(
                    "File not found, please make sure your config file actually exists"
                )
        case _:
            print("Unsupported operating system, sorry!")
    return
