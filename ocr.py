from number import Number

INVALID_CHECKSUM = "ERR"
UNRECOGNISED = "ILL"


def scan(text):
    scanned = Number.from_text(text)
    return str(scanned)


def validated_scan(text):
    scanned = Number.from_text(text)
    if scanned.not_correctly():
        return f"{scanned} ILL"

    if scanned.has_invalid_checksum():
        return f"{scanned} ERR"

    return str(scanned)


def guessed_scan(text):
    scanned = Number.from_text(text)
    if scanned.not_correctly():
        fixed = [str(n) for n in scanned.fix() if not n.has_invalid_checksum()][0]
        return f"{fixed}"

    if scanned.has_invalid_checksum():
        # get all possible numbers
        found = sorted(
            [str(n) for n in scanned.possible_numbers() if not n.has_invalid_checksum()]
        )
        if len(found) > 1:
            return f"{scanned} AMB {found}"

        return ",".join(found)

    return str(scanned)
