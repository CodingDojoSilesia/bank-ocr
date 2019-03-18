from number import Number


def scan(text):
    number = Number.from_text(text)
    return str(number)


def validated_scan(text):
    number = Number.from_text(text)
    if number.incorrect_scan():
        return f"{number} ILL"

    if number.checksum_invalid():
        return f"{number} ERR"

    return str(number)


def guessed_scan(text):
    number = Number.from_text(text)
    if number.incorrect_scan():
        fixed = [n for n in number.fix()][0]
        return f"{fixed}"

    if number.checksum_invalid():
        # get all possible numbers
        found = sorted([str(n) for n in number.possible_numbers()])
        if len(found) > 1:
            return f"{number} AMB {found}"

        return ",".join(found)

    return str(number)
