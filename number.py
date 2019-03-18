from os import linesep

from digit import DigitFactory
from digit import UnrecognisedDigit


class Number:
    "Container translating input into individual characters"

    @classmethod
    def from_text(cls, text):
        """Alternative constructor to Number class.

        Supports scanning of text and generating Digits.
        Similar as https://docs.python.org/3.7/library/stdtypes.html#dict.fromkeys
        """
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

    def __str__(self):
        return "".join(str(d) for d in self._number)

    def __init__(self, digits):
        self._number = digits

    def __getitem__(self, key):
        return self._number[key]

    def __len__(self):
        return len(self._number)

    def index(self, el):
        return self._number.index(el)

    def checksum_valid(self):
        """ Verifies if Number has a valid checksum."""
        try:
            _, remainder = divmod(
                sum(x * int(y) for x, y in zip(range(1, 10), reversed(self))), 11
            )
        except UnrecognisedDigit:  # bail on Unknown digit
            return False
        return remainder == 0

    def checksum_invalid(self):
        return not self.checksum_valid()

    def incorrect_scan(self):
        return any([not d.known for d in self])

    def possible_numbers(self):
        for d in self:
            for f in d.flips():
                c = self[:]
                c[self.index(d)] = f
                new = Number(c)
                if new.checksum_valid():
                    yield new

    def fix(self):
        for d in self:
            for f in d.fixes():
                c = self[:]
                c[self.index(d)] = f
                new = Number(c)
                if new.checksum_valid():
                    yield new
