from os import linesep

from digit import DigitFactory as Digit
from digit import UnrecognisedDigit


class Number:
    "Container translating input into individual characters"

    @classmethod
    def from_text(cls, text):
        one, two, three, _ = text.split(linesep)
        digits = [
            Digit(
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
        return any([not d.known for d in self])

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
