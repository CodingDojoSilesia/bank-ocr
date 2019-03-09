from os import linesep


class Screen:
    "Container translating input into individual characters"

    def __init__(self, input_):
        self.one, self.two, self.three, _ = input_.split(linesep)

    def __getitem__(self, key):
        try:
            k = key * 3
            j = k + 3
        except TypeError:  # we have slice
            k = key.start * 3
            j = key.stop * 3

        return linesep.join(
            [self.one[k : j], self.two[k : j], self.three[k : j]]
        )

    def __iter__(self):
        for x in range(9):
            yield self[x]


def scan(text):
    # split by \n
    # 4 lines
    # take 3 chars from 3 top lines, that is a number
    return Screen(text)
