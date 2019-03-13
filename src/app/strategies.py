zero = ('0', (
  ' _ ',
  '| |',
  '|_|',
))

one = ('1', (
  '   ',
  '  |',
  '  |',
))

two = ('2', (
  ' _ ',
  ' _|',
  '|_ ',
))

three = ('3', (
  ' _ ',
  ' _|',
  ' _|',
))

four = ('4', (
  '   ',
  '|_|',
  '  |',
))

five = ('5', (
  ' _ ',
  '|_ ',
  ' _|',
))

six = ('6', (
  ' _ ',
  '|_ ',
  '|_|',
))

seven = ('7', (
  ' _ ',
  '  |',
  '  |',
))

eight = ('8', (
  ' _ ',
  '|_|',
  '|_|',
))

nine = ('9', (
  ' _ ',
  '|_|',
  ' _|',
))


MATCHING_DIGITS = (
  ('0', (
    ('   ',
     '| |',
     '|_|'),
    (' _ ',
     '  |',
     '|_|'),
    (' _ ',
     '|  ',
     '|_|'),
    (' _ ',
     '| |',
     ' _|'),
    (' _ ',
     '| |',
     '| |'),
    (' _ ',
     '| |',
     '|_ '),
  )),
  ('1', (
    ('   ',
     '  |',
     '   '),
    ('   ',
     '   ',
     '  |')
  )),
  ('2', (
    ('   ',
     ' _|',
     '|_ '),
    (' _ ',
     ' _ ',
     '|_ '),
    (' _ ',
     '  |',
     '|_ '),
    (' _ ',
     ' _|',
     ' _ '),
    (' _ ',
     ' _|',
     '|  '),
  )),
  ('3', (
    ('   ',
     ' _|',
     ' _|'),
    (' _ ',
     ' _ ',
     ' _|'),
    (' _ ',
     '  |',
     ' _|'),
    (' _ ',
     ' _|',
     ' _ '),
    (' _ ',
     ' _|',
     '  |'),
  )),
  ('4', (
    ('   ',
     ' _|',
     '  |'),
    ('   ',
     '| |',
     '  |'),
    ('   ',
     '|_ ',
     '  |'),
    ('   ',
     '|_|',
     '   '),
  )),
  ('5', (
    ('   ',
     '|_ ',
     ' _|'),
    (' _ ',
     ' _ ',
     ' _|'),
    (' _ ',
     '|  ',
     ' _|'),
    (' _ ',
     '|_ ',
     ' _ '),
    (' _ ',
     '|_ ',
     '  |'),
  )),
  ('6', (
    (' _ ',
     ' _ ',
     '|_|'),
    (' _ ',
     '|  ',
     '|_|'),
    (' _ ',
     '|_ ',
     ' _|'),
    (' _ ',
     '|_ ',
     '| |'),
    (' _ ',
     '|_ ',
     '|_ '),
  )),
  ('7', (
    ('   ',
     '  |',
     '  |'),
    (' _ ',
     '   ',
     '  |'),
    (' _ ',
     '  |',
     '   '),
  )),
  ('8', (
    ('   ',
     '|_|',
     '|_|'),
    (' _ ',
     ' _|',
     '|_|'),
    (' _ ',
     '| |',
     '|_|'),
    (' _ ',
     '|_ ',
     '|_|'),
    (' _ ',
     '|_|',
     ' _|'),
    (' _ ',
     '|_|',
     '| |'),
    (' _ ',
     '|_|',
     '|_ '),
  )),
  ('9', (
    ('   ',
     '|_|',
     ' _|'),
    (' _ ',
     ' _|',
     ' _|'),
    (' _ ',
     '| |',
     ' _|'),
    (' _ ',
     '|_ ',
     ' _|'),
    (' _ ',
     '|_|',
     '  |'),
    (' _ ',
     '|_|',
     ' _'),
  ))
)


KNOWN_DIGITS = (
  zero, one, two,
  three, four, five,
  six, seven, eight, nine,
)

class ExactMatching(object):
  KNOWN_DIGITS = KNOWN_DIGITS
  NOT_FOUND = None

  def match(self, digit):
    target_schema = tuple(digit.split('\n'))
    for digit, schema in self.KNOWN_DIGITS:
      if schema == target_schema:
        return digit
    return self.NOT_FOUND


class FuzzyMatching(ExactMatching):
  MATCHING_DIGITS = MATCHING_DIGITS
  NOT_FOUND = None

  def match(self, digit):
    exact_match = super().match(digit)
    if exact_match is None:
      return self._close_match(digit)
    return exact_match
    

  def _close_match(self, digit):
    target_schema = tuple(digit.split('\n'))
    matching_digits = []
    for digit, schemas in self.MATCHING_DIGITS:
      if any(target_schema == schema for schema in schemas):
        matching_digits.append(digit)
    
    if not matching_digits:
      return self.NOT_FOUND
    return matching_digits
