from itertools import chain
from os import linesep

INVALID_CHECKSUM = "ERR"
UNRECOGNISED = "ILL"


class UnrecognisedDigit(Exception):
    pass


class Number:
    "Container translating input into individual characters"

    @classmethod
    def from_text(cls, text):
        one, two, three, _ = text.split(linesep)
        digits = [
            DigitFactory(
                (
                    one[x * 3 : (x + 1) * 3],
                    two[x * 3 : (x + 1) * 3],
                    three[x * 3 : (x + 1) * 3],
                )
            )
            for x in range(0, 9)
        ]
        return Number(digits)

    def __init__(self, digits):
        self._number = digits

    def __getitem__(self, key):
        return self._number[key]

    def __str__(self):
        return "".join(str(d) for d in self._number)

    def __len__(self):
        return len(self._number)

    def index(self, el):
        return self._number.index(el)

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

    def possible_numbers(self):
        p = []
        # TODO: this might not need enumerate
        for i, d in enumerate(self):
            for f in d.flips():
                c = list(self)
                c[i] = f
                new = Number(c)
                p.append(new)

        return p

    def fix(self):
        p = []
        for d in self:
            for f in d.fixes():
                c = self[:]
                c[self.index(d)] = f
                new = Number(c)
                p.append(new)
        return p


class DigitFactory:
    def __new__(cls, text):
        if text == (" _ ", "| |", "|_|") or text == "0":
            return Zero((" _ ", "| |", "|_|"))
        if text == ("   ", "  |", "  |") or text == "1":
            return One(("   ", "  |", "  |"))
        if text == (" _ ", " _|", "|_ ") or text == "2":
            return Two((" _ ", " _|", "|_ "))
        if text == (" _ ", " _|", " _|") or text == "3":
            return Three(text)
        if text == ("   ", "|_|", "  |") or text == "4":
            return Four(text)
        if text == (" _ ", "|_ ", " _|") or text == "5":
            return Five(text)
        if text == (" _ ", "|_ ", "|_|") or text == "6":
            return Six(text)
        if text == (" _ ", "  |", "  |") or text == "7":
            return Seven((" _ ", "  |", "  |"))
        if text == (" _ ", "|_|", "|_|") or text == "8":
            return Eight((" _ ", "|_|", "|_|"))
        if text == (" _ ", "|_|", " _|") or text == "9":
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

    def flips(self):
        return [DigitFactory(o) for o in self._options]

    def fixes(self):
        if self.value != "?":
            return []

        n = {0: ["   "], 1: [" _ ", "  |"], 2: ["| |", " _|", "|_ "], 3: ["|_|"]}
        f = []

        for i, e in enumerate(self._text):
            pipes = e.count("_") + e.count("|")
            if pipes >= 2:
                pipe_range = range(0, 3)
            else:
                pipe_range = range(0, pipes + 2)
            replacements = chain.from_iterable([n[p] for p in pipe_range])
            def new_digit(current_digit, element_index, replacement):
                c = list(current_digit[:])
                c[element_index] = replacement
                return tuple(c)
            proposed_digits = [
                DigitFactory(new_digit(self._text, i, x))
                for x in replacements
            ]
            proper_digits = [d for d in proposed_digits if not isinstance(d, Unknown)]
            f.extend(proper_digits)
        return f


class Unknown(Digit):
    value = "?"


class Zero(Digit):
    value = "0"
    _options = ["8"]


class One(Digit):
    value = "1"
    _options = ["7"]


class Two(Digit):
    value = "2"
    _options = []


class Three(Digit):
    value = "3"
    _options = ["9"]


class Four(Digit):
    value = "4"
    _options = []


class Five(Digit):
    value = "5"
    _options = ["9", "6"]


class Six(Digit):
    value = "6"
    _options = ["8", "5"]


class Seven(Digit):
    value = "7"
    _options = ["1"]


class Eight(Digit):
    value = "8"
    _options = ["0", "6", "9"]


class Nine(Digit):
    value = "9"
    _options = ["8", "3", "5"]


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
