from typing import Any


def find_item(dict: dict, item: tuple[str, Any]) -> Any | None:
    return next(
        (obj for obj in dict.values() if obj[item[0]] == item[1]),
        None  # Default value if no match is found
    )