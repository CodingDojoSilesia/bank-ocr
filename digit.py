from itertools import chain


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

    @property
    def known(self):
        return not issubclass(self.__class__, Unknown)

    def flips(self):
        return (DigitFactory(o) for o in self._options)

    def fixes(self):
        if self.known:
            yield self  # no fixes for known digit

        # {number of "_" or "|" : list of combinations}
        char_count = {
            0: ["   "],
            1: [" _ ", "  |"],
            2: ["| |", " _|", "|_ "],
            3: ["|_|"],
        }

        for i, e in enumerate(self._text):
            pipes = e.count("_") + e.count("|")
            if pipes >= 2:
                pipe_range = range(0, 3)
            else:
                pipe_range = range(0, pipes + 2)
            replacements = chain.from_iterable([char_count[p] for p in pipe_range])

            def new_digit(current_digit, element_index, replacement):
                c = list(current_digit[:])
                c[element_index] = replacement
                return tuple(c)

            proposed_digits = [
                DigitFactory(new_digit(self._text, i, x)) for x in replacements
            ]
            for d in proposed_digits:
                if d.known:
                    yield d


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


class UnrecognisedDigit(Exception):
    pass


class DigitFactory:
    def __new__(cls, text):
        digits = {
            ((" _ ", "| |", "|_|"), "0"): Zero,
            (("   ", "  |", "  |"), "1"): One,
            ((" _ ", " _|", "|_ "), "2"): Two,
            ((" _ ", " _|", " _|"), "3"): Three,
            (("   ", "|_|", "  |"), "4"): Four,
            ((" _ ", "|_ ", " _|"), "5"): Five,
            ((" _ ", "|_ ", "|_|"), "6"): Six,
            ((" _ ", "  |", "  |"), "7"): Seven,
            ((" _ ", "|_|", "|_|"), "8"): Eight,
            ((" _ ", "|_|", " _|"), "9"): Nine,
        }
        for d, c in digits.items():
            if text in d:
                return c(text)
        else:
            return Unknown(text)
