import requests
from typing import Any

from etae.utils.card import Card

API_URL = "http://127.0.0.1:8000/"


def send_data_to_etae(
    config: dict[str, Any] | str, cards_info: dict[str, list[Card] | None]
) -> None:
    user_info: dict[str, str] | None = config.get("user_info")
    if user_info is None:
        print("Your config could not have been found")
        return
    user_login: str | None = user_info.get("login")
    user_password: str | None = user_info.get("password")
    if user_login is None or user_password is None:
        print("Login or password not found")
        return
    requests.post(
        API_URL,
        json={"login": user_login, "password": user_password, "cards": cards_info},
    )
