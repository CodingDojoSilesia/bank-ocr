from os import linesep

INVALID_CHECKSUM = "ERR"
UNRECOGNISED = "ILL"


class UnrecognisedDigit(Exception):
    pass


class Number:
    "Container translating input into individual characters"

    def __init__(self, input_):
        self.one, self.two, self.three, _ = input_.split(linesep)

    def __getitem__(self, key):
        if key > 8:
            raise IndexError

        try:
            k = key * 3
            j = k + 3
        except TypeError:  # we have slice
            k = key.start * 3
            j = key.stop * 3

        return DigitFactory((self.one[k:j], self.two[k:j], self.three[k:j]))

    def __str__(self):
        return "".join(str(d) for d in self)

    def __len__(self):
        return 9

    def has_invalid_checksum(self):
        try:
            _, remainder = divmod(
                sum(x * int(y) for x, y in zip(range(1, 10), reversed(self))), 11
            )
        except UnrecognisedDigit:
            return False
        return remainder != 0

    def not_correctly(self):
        return any([isinstance(d, Unknown) for d in self])


class DigitFactory:
    def __new__(cls, text):
        if text == (" _ ", "| |", "|_|"):
            return Zero(text)
        if text == ("   ", "  |", "  |"):
            return One(text)
        if text == (" _ ", " _|", "|_ "):
            return Two(text)
        if text == (" _ ", " _|", " _|"):
            return Three(text)
        if text == ("   ", "|_|", "  |"):
            return Four(text)
        if text == (" _ ", "|_ ", " _|"):
            return Five(text)
        if text == (" _ ", "|_ ", "|_|"):
            return Six(text)
        if text == (" _ ", "  |", "  |"):
            return Seven(text)
        if text == (" _ ", "|_|", "|_|"):
            return Eight(text)
        if text == (" _ ", "|_|", " _|"):
            return Nine(text)

        return Unknown(text)


class Digit:
    def __init__(self, text):
        self._text = text

    def __str__(self):
        return self.value

    def __int__(self):
        try:
            return int(self.value)
        except ValueError:
            raise UnrecognisedDigit

    def __repr__(self):
        return linesep.join(self._text) + linesep


class Unknown(Digit):
    value = "?"


class Zero(Digit):
    value = "0"


class One(Digit):
    value = "1"


class Two(Digit):
    value = "2"


class Three(Digit):
    value = "3"


class Four(Digit):
    value = "4"


class Five(Digit):
    value = "5"


class Six(Digit):
    value = "6"


class Seven(Digit):
    value = "7"


class Eight(Digit):
    value = "8"


class Nine(Digit):
    value = "9"


def scan(text):
    scanned = Number(text)
    return str(scanned)


def validated_scan(text):
    scanned = Number(text)
    if scanned.not_correctly():
        return f"{scanned} ILL"

    if scanned.has_invalid_checksum():
        return f"{scanned} ERR"

    return str(scanned)
