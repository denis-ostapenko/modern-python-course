def parse_count(raw):
    try:
        count = int(raw)
    except ValueError:
        return None
    if count < 0:
        return None
    return count
