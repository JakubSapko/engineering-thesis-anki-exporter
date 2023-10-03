from typing import Any


def replace_characters(s: str):
    return s[0] + "*" * (len(s) - 2) + s[-1]


def format_config_message(config: dict[str, Any], anonymous: bool) -> str:
    message: str = ""
    user_info: dict[str, Any] = config.get("user_info")
    if user_info:
        login: str = user_info["login"]
        password: str = user_info["password"]
        if anonymous:
            password: str = replace_characters(password)
        message += f"Your login: {login}\nYour password: {password}\n"
    else:
        message += "No user info found\n"
    return message
