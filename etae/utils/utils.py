from typing import Any, Literal, Optional, Tuple, TypeAlias, TypeVar
from pathlib import Path
import toml
import os

SYSTEM = Literal["Windows", "Darwin", "Linux"]


def load_config_file(path: str) -> dict[str, Any]:
    try:
        config: dict[str, Any] = toml.load(path)
        return config
    except FileNotFoundError:
        print("File not found, please make sure your config file actually exists")
        return {}


def get_config_file(system: SYSTEM) -> dict[str, Any] | str:
    unix_home_path: Path = Path.home()
    match system:
        case "Windows":
            appdata: str = os.getenv("LOCALAPPDATA")
            file_path: str = os.path.join(appdata, "Anki2/test.toml")
            config: dict[str, Any] = load_config_file(file_path)
        case "Linux":
            config: dict[str, Any] = load_config_file(
                str(unix_home_path) + "/.local/share/Anki2/test.toml"
            )
        case "Darwin":
            config: dict[str, Any] = load_config_file(
                str(unix_home_path) + "/Library/Application Support/Anki2/test.toml"
            )
        case _:
            print("Unsupported operating system, sorry!")
    return config


def set_config_file(system: SYSTEM, login: str, password: str):
    unix_home_path: Path = Path.home()
    match system:
        case "Windows":
            appdata: str = os.getenv("LOCALAPPDATA")
            file_path: str = os.path.join(appdata, "Anki2/test.toml")
            config: dict[str, Any] = create_config_file(file_path, login, password)
        case "Linux":
            config: dict[str, Any] = create_config_file(
                str(unix_home_path) + "/.local/share/Anki2/test.toml", login, password
            )
        case "Darwin":
            config: dict[str, Any] = create_config_file(
                str(unix_home_path) + "/Library/Application Support/Anki2/test.toml",
                login,
                password,
            )
        case _:
            print("Unsupported operating system, sorry!")
    return


def create_config_file(path: str, login: str, password: str) -> bool:
    try:
        toml.dump(
            {"user_info": {"login": login, "password": password}}, open(path, "w")
        )
        return True
    except Exception as e:
        print(f"Error occured: {e}")
        return False
