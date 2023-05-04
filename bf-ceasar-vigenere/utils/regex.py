import unicodedata

def remove_combining_regex(self: str) -> str:
    normalized = unicodedata.normalize('NFD', self)
    decode_string = normalized.encode('ascii', 'ignore').decode('utf8').casefold()
    return decode_string.strip()