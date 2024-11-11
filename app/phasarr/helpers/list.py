def is_list(var) -> bool:
    return isinstance(var, list)

def find_index(list, entry) -> int | None:
    try:
        return list.index(entry)
    except ValueError:
        return None