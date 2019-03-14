from os import linesep

INVALID_CHECKSUM = "ERR"
UNRECOGNISED = "ILL"


class UnrecognisedDigit(Exception):
    pass


class Number:
    "Container translating input into individual characters"

    # change this into from_text
    @classmethod
    def from_text(cls, text):

        # FIXME: rename to from_text
        # method should parse incoming text as __init__ does now
        # and use digit factory to create a list of digits
        # __init__ should accept list of digits
        # iteration and slicing will be much simpler as will be performed
        # on an actual internal list
        one, two, three, _ = text.split(linesep)
        digits = [DigitFactory((one[x*3: (x+1)*3],
                                two[x*3: (x+1)*3],
                                three[x*3: (x+1)*3])) for x in range(0, 9)]
        return Number(digits)

    def __init__(self, digits):
        self._number = digits

    def __getitem__(self, key):
        return self._number[key]

    def __str__(self):
        return "".join(str(d) for d in self._number)

    def __len__(self):
        return len(self._number)

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
        for i, d in enumerate(self):
            for f in d.flips():
                try:
                    c = list(self)
                    c[i] = f
                    new = Number.from_list(c)
                except IndexError:
                    new = []
                p.append(new)
        # create list of possible no (PN)
        # FIXME: iterate over digits
        # get all other options for each digit
        # append to list of PN
        # return list of PN
        return p


# This might be for fixing incorrectly scanned numbers
# allowed_combinations = ["   ", " _ ", "  |", "| |", " _|", "|_ ", "|_|"]
# [0 elements, 1 element, 2 elements, 3 elements]
# count elements in current frame see if moving left or right will fix it

# this might be for finding valid checksums
# another approach is to figure out possible transitions
# 9 can only be 8 or vice versa
# 6 can only be 8 and vice versa


class DigitFactory:
    def __new__(cls, text):
        if text == (" _ ", "| |", "|_|") or text == "0":
            return Zero((" _ ", "| |", "|_|"))
        if text == ("   ", "  |", "  |") or text == "1":
            return One(("   ", "  |", "  |"))
        if text == (" _ ", " _|", "|_ ") or text == "2":
            return Two(text)
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

    # def __repr__(self):
    #     return linesep.join(self._text) + linesep

    def flips(self):
        return [DigitFactory(o) for o in self._options]


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


class Three(Digit):
    value = "3"
    _options = ["9"]


class Four(Digit):
    value = "4"


class Five(Digit):
    value = "5"
    _options = ["9"]


class Six(Digit):
    value = "6"
    _options = ["8", "5"]


class Seven(Digit):
    value = "7"
    _options = ["1"]


class Eight(Digit):
    value = "8"
    _options = ["0"]


class Nine(Digit):
    value = "9"
    _options = ["8", "3"]


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
        return f"{scanned} ILL"

    if scanned.has_invalid_checksum():
        # get all possible numbers
        return [n for n in scanned.possible_numbers() if not n.has_invalid_checksum()]
        # iterate and see if any has valid checksum
        # return successes
        # return f"{scanned} ERR"

    return str(scanned)
