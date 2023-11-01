import json
import re
from typing import Any, Literal, Optional
from pathlib import Path
import toml
import os

SYSTEM = Literal["Windows", "Darwin", "Linux"]


def load_config_file(path: str) -> dict[str, Any] | None:
    try:
        config: dict[str, Any] = toml.load(path)
        return config
    except FileNotFoundError:
        print("File not found, please make sure your config file actually exists")
        return None


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
            _ = create_config_file(file_path, login, password)
        case "Linux":
            _ = create_config_file(
                str(unix_home_path) + "/.local/share/Anki2/test.toml", login, password
            )
        case "Darwin":
            _ = create_config_file(
                str(unix_home_path) + "/Library/Application Support/Anki2/test.toml",
                login,
                password,
            )
        case _:
            print("Unsupported operating system, sorry!")
    return


def create_config_file(path: str, login: str, password: str):
    try:
        toml.dump(
            {"user_info": {"login": login, "password": password}}, open(path, "w")
        )
    except Exception as e:
        print(f"Error occured: {e}")


def list_of_dicts_to_dataframe_format(
    list_to_parse: list[dict[str, Any]]
) -> dict[str, list[Any]]:
    dataframe_dict: dict[str, list[Any]] = {}
    for index, card in enumerate(list_to_parse):
        for key, value in card.items():
            if key not in dataframe_dict:
                dataframe_dict.update({key: [value]})
            else:
                dataframe_dict[key].append(value)
    return dataframe_dict


def extract_definition_and_dictionary_form_from_fields(
    cell: str,
) -> tuple[Optional[str], list[str]]:
    LIST_ITEM_PATTERN = r"<li>(.*?)</li>"
    DICTIONARY_FORM_PATTERN = (
        r"\'wordDictionaryForm\': {\'value\': \'<span[^>]*>(.*?)</span>\'"
    )
    all_definitions = re.findall(LIST_ITEM_PATTERN, cell)
    dictionary_form_match = re.search(DICTIONARY_FORM_PATTERN, cell)
    dictionary_form = dictionary_form_match.group(1) if dictionary_form_match else None
    return (dictionary_form, all_definitions)


if __name__ == "__main__":
    x = extract_definition_and_dictionary_form_from_fields(
        '{"wordDictionaryForm": {"value": "<span class=\\"\\"">条件</span>", "order": 0}, "sentence": {"value": "でも休止ってことは<span class=\\"highlight\\">条件</span>がそろえば活動が再開できるって事だ", "order": 1}, "reading": {"value": "じょうけん", "order": 2}, "definition": {"value": "<div style=\\"text-align: left;\\"><span><ul data-sc-content=\\"glossary\\" lang=\\"en\\" style=\\"list-style-type: circle;\\"><li>condition</li><li>term</li><li>requirement</li><li>qualification</li><li>prerequisite</li></ul><ul data-sc-content=\\"examples\\" lang=\\"ja\\" style=\\"list-style-type: &quot;🇯🇵 &quot;;\\"><li>そちらの条件を受け入れましょう。</li><li lang=\\"en\\" style=\\"list-style-type: &quot;🇬🇧 &quot;;\\">We will accept your conditions.</li></ul></span></div>", "order": 3}, "wordAudio": {"value": "[sound:yomichan_audio_じょうけん_条件_2023-02-29-16-13-58.mp3]", "order": 4}, "sentenceAudio": {"value": "", "order": 5}, "picture": {"value": "", "order": 6}, "pitchAccent": {"value": "じょうけん", "order": 7}, "frequency": {"value": "761", "order": 8}}'
    )
    print(x)
