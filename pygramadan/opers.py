def _safestart(text: str, piece: str, lc = False) -> bool:
    check = text if lc else text.lower()
    return len(text) >= len(piece) and check.startswith(piece)

def _delenite(text: str) -> str:
    cons = "bcdfgmpst"
    lc = text.lower()
    if len(text) >= 2 and lc[0] in cons and lc[1] == 'h':
        return text[0] + text[2:]
    else:
        return text

def _is_vowel(char: str) -> bool:
    vowels = "aeiouáéíóú"
    return len(char) == 1 and char.lower()[0] in vowels

def _is_uppervowel(char: str) -> bool:
    vowels = "AEIOUÁÉÍÓÚ"
    return len(char) == 1 and char[0] in vowels

def demutate(text: str) -> str:
    text = text[2:] if _safestart(text, "bhf") else text
    text = _delenite(text)
    text = text[1:] if _safestart(text, "mb") else text
    text = text[1:] if _safestart(text, "gc") else text
    text = text[1:] if _safestart(text, "nd") else text
    text = text[1:] if _safestart(text, "ng") else text
    text = text[1:] if _safestart(text, "bp") else text
    text = text[1:] if _safestart(text, "ts") else text
    text = text[1:] if _safestart(text, "dt") else text
    text = _delenite(text[2:]) if _safestart(text, "d'fh") else text
    lc = text.lower()
    text = text[2:] if len(lc) >= 3 and _safestart(text, "d'") and _is_vowel(lc[2]) else text
    text = text[1:] if len(lc) >= 2 and lc[0] == 'h' and _is_vowel(lc[1]) else text
    text = text[2:] if len(lc) >= 3 and _safestart(text, "n-") and _is_vowel(lc[2]) else text
    return text

def ends_dental(text: str) -> bool:
    return text.lower()[-1] in "dnts"

def starts_bilabial(text: str) -> bool:
    return len(text) > 0 and text.lower()[0] in "bmp"

def starts_vowel(text: str) -> bool:
    return len(text) > 0 and _is_vowel(text[0])

def starts_vowelfhx(text: str) -> bool:
    lc = text.lower()
    if lc[0:3] == 'fhl' or lc[0:3] == 'fhr':
        return False
    else:
        return lc[0:2] == 'fh' or starts_vowel(text)

def starts_fvowel(text: str) -> bool:
    return len(text) > 0 and (_is_vowel(text[0]) or text[0].lower() == 'f')

def _is_mutable_s(text: str) -> bool:
    lc = text.lower()
    return len(lc) >= 2 and lc[0] == 's' and lc[1] in "rnlaeiouáéíóú"

def eclipsis(text: str, restriction: str = "") -> str:
    mut = {
        'b': 'm',
        'c': 'g',
        'd': 'n',
        'f': 'bh',
        'g': 'n',
        'p': 'b',
        't': 'd'
    }
    firstl = text.lower()[0]
    if len(text) < 1:
        return text
    if _is_uppervowel(text[0]):
        return "n" + text
    elif firstl == text[0] and _is_vowel(text[0]):
        return "n-" + text
    elif firstl in mut and firstl not in restriction:
        return mut[firstl] + text
    else:
        return text

def lenition(text: str, restriction: str = "") -> str:
    def dolen(text: str) -> str:
        if text[0:2].isupper():
            return text[0] + 'H' + text[1:]
        else:
            return text[0] + 'h' + text[1:]
    if len(text) > 1 and text.lower()[1] == 'j':
        return text
    lc = text.lower()
    if len(text) >= 1 and lc[0] in "bcdfgmpt" and lc[0] not in restriction:
        return dolen(text)
    elif _is_mutable_s(text) and 's' not in restriction:
        return dolen(text)
    else:
        return text
