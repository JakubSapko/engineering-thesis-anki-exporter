import json
import urllib.request

from etae.utils.card import Card


def request(action, **params):
    return {"action": action, **params, "version": 6}


def invoke(action, **params):
    requestJson = json.dumps(request(action, **params)).encode("utf-8")
    response = json.load(
        urllib.request.urlopen(
            urllib.request.Request("http://localhost:8765", requestJson)
        )
    )
    if len(response) != 2:
        raise Exception("response has an unexpected number of fields")
    if "error" not in response:
        raise Exception("response is missing required error field")
    if "result" not in response:
        raise Exception("response is missing required result field")
    if response["error"] is not None:
        raise Exception(response["error"])
    return response


def get_decks_data(decks: set[str]):
    deck_cards = find_cards_of_given_decks(decks)
    cards = get_card_info_for_decks(deck_cards)
    return cards


def find_cards_of_given_decks(decks: set[str]) -> dict[str, list[int] | None]:
    deck_cards: dict[str, list[int] | None] = {}
    for deck_name in decks:
        result = invoke("findCards", params={"query": f"deck:{deck_name}"})
        if result["error"] is None:
            deck_cards.update({deck_name: result["result"]})
    return deck_cards


def get_card_info_for_decks(
    decks_with_cards: dict[str, list[int] | None]
) -> dict[str, list[Card] | None]:
    deck_cards_info: dict[str, list[Card] | None] = {}
    for deck_name, deck_cards in decks_with_cards.items():
        cards = invoke("cardsInfo", params={"cards": deck_cards})
        if cards is not None:
            deck_cards_info.update({deck_name: cards})
            continue
        raise Exception("Something went wrong when fetching Anki cards! Sorry!")
    return deck_cards_info
