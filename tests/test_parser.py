from app.parser import FuzzyDigitParser, ExactDigitParser

import pytest


@pytest.mark.parametrize('_input, expected_output', [
  ((' _ ' ,
    '| |' ,
    '|_|' ,
  ), '0'),
  (('   ' ,
    '  |' ,
    '  |' ,
  ), '1'),
  ((' _ ' ,
    ' _|' ,
    '|_ ' ,
  ), '2'),
  ((' _ ' ,
    ' _|' ,
    ' _|' ,
  ), '3'),
  (('   ' ,
    '|_|' ,
    '  |' ,
  ), '4'),
  ((' _ ' ,
    '|_ ' ,
    ' _|' ,
  ), '5'),
  ((' _ ' ,
    '|_ ' ,
    '|_|' ,
  ), '6'),
  ((' _ ' ,
    '  |' ,
    '  |' ,
  ), '7'),
  ((' _ ' ,
    '|_|' ,
    '|_|' ,
  ), '8'),
  ((' _ ' ,
    '|_|' ,
    ' _|' ,
  ), '9')
])
def test__exact_matching_known_digits_recognition(_input, expected_output):
  parser = ExactDigitParser()
  assert parser.parse('\n'.join(_input)) == expected_output


@pytest.mark.parametrize('_input', [
  (' _ ',
   '|  ',
   '|_|',
  ),
  ('   ',
   ' _|',
   '  |',
  ),
  ('   ',
   '| |',
   '  |',
  ),
  ('   ',
   ' _|',
   '| |',
  ),
])
def test__exact_matching_unknown_digits_recognition(_input):
  parser = ExactDigitParser()
  assert parser.parse('\n'.join(_input)) == ExactDigitParser.NOT_FOUND



@pytest.mark.parametrize('_input, expected_output', [
  ((' _ ' ,
    '| |' ,
    '|_|' ,
  ), '0'),
  (('   ' ,
    '  |' ,
    '  |' ,
  ), '1'),
  ((' _ ' ,
    ' _|' ,
    '|_ ' ,
  ), '2'),
  ((' _ ' ,
    ' _|' ,
    ' _|' ,
  ), '3'),
  (('   ' ,
    '|_|' ,
    '  |' ,
  ), '4'),
  ((' _ ' ,
    '|_ ' ,
    ' _|' ,
  ), '5'),
  ((' _ ' ,
    '|_ ' ,
    '|_|' ,
  ), '6'),
  ((' _ ' ,
    '  |' ,
    '  |' ,
  ), '7'),
  ((' _ ' ,
    '|_|' ,
    '|_|' ,
  ), '8'),
  ((' _ ' ,
    '|_|' ,
    ' _|' ,
  ), '9')
])
def test__fuzzy_matching_known_digits_recognition(_input, expected_output):
  parser = FuzzyDigitParser()
  assert parser.parse('\n'.join(_input)) == expected_output



@pytest.mark.parametrize('_input, expected_output', [
  ((
    ' _ ',
    '|  ',
    '|_|'
  ), ['0', '6']),
  ((
    ' _ ',
    ' _ ',
    ' _|'
  ), ['3', '5']),
  ((
    '   ',
    '   ',
    '  |'
  ), ['1']),
  ((
    '   ',
    '|_|',
    '   '
  ), ['4'])
])
def test__fuzzy_matching_unknown_digits_recognition(_input, expected_output):
  parser = FuzzyDigitParser()
  assert parser.parse('\n'.join(_input)) == expected_output
