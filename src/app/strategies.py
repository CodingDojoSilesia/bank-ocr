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
     ' _ '),
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
    '''
      :param digit: (str) - multiline string 
                            representing a simple digit

      :return str: string digit or None if not found

      Check if given string is an actual number

      Example:
        
        d = ' _ \n' \
            '| |\n \
            '|_|'

        >> ExactMatching().match(d)
        => '0'
    '''
    target_schema = tuple(digit.split('\n'))
    for digit, schema in self.KNOWN_DIGITS:
      if schema == target_schema:
        return digit
    return self.NOT_FOUND


class FuzzyMatching(ExactMatching):
  MATCHING_DIGITS = MATCHING_DIGITS
  NOT_FOUND = None

  def match(self, digit):
    '''
      :param digit: (str) - multiline string 
                            representing a simple digit

        :return list: list of string digits
                      that are CLOSE to given input
                      or None if not found

        Search for digits that ONLY look-alike given digit
        but are NOT the same.

        Example:
          
          d = ' _ \n' \
              '| |\n \
              '|_|'

          >> FuzzyMatching().match(d)
          => ['8']

          d2 = ' _ \n' \
               '|  \n \
               '|_|'

          >> FuzzyMatching().match(d)
          => ['0', '6']
    '''
    target_schema = tuple(digit.split('\n'))
    matching_digits = []
    for digit, schemas in self.MATCHING_DIGITS:
      if any(target_schema == schema for schema in schemas):
        matching_digits.append(digit)
    
    return matching_digits or self.NOT_FOUND
