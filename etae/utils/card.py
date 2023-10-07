from dataclasses import dataclass
from typing import Any


@dataclass
class Card:
    answer: str
    question: str
    deckName: str
    modelName: str
    fieldOrder: int
    fields: dict[str, dict[str, Any]]
    css: str
    cardId: int
    interval: int
    note: int
    ord: int
    type: int
    queue: int
    due: int
    reps: int
    lapses: int
    left: int
    mod: int
