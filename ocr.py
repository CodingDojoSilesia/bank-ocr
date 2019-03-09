from os import linesep


class Screen:
    "Container translating input into individual characters"

    def __init__(self, input_):
        self.one, self.two, self.three, _ = input_.split(linesep)

    def __getitem__(self, key):
        # TODO: slicing
        k = key * 3
        return linesep.join(
            [self.one[k : k + 3], self.two[k : k + 3], self.three[k : k + 3]]
        )

    def __iter__(self):
        for x in range(9):
            yield self[x]


def scan(text):
    # split by \n
    # 4 lines
    # take 3 chars from 3 top lines, that is a number
    return Screen(text)
