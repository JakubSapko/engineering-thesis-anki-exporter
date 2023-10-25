import requests
import pandas as pd
from typing import Any

from etae.utils.card import Card
from etae.utils.utils import list_of_dicts_to_dataframe_format

API_URL = "http://127.0.0.1:8000/api"


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
    parsed_data = list_of_dicts_to_dataframe_format(cards_info["Clannad"]["result"])
    output = pd.DataFrame(parsed_data)
    fitted_output = output.drop(
        columns=["fieldOrder", "question", "answer", "modelName", "css"]
    )
    fitted_output.to_csv("output.csv", index=False)
    # response = requests.post(
    #     API_URL,
    #     json={"login": user_login, "password": user_password, "cards": cards_info},
    # )
    # if response.status_code == 200:
    #     print("Data sent successfully!")
    #     return
    # print(f"HTTP error occured: {response.status_code}: {response.text}")
