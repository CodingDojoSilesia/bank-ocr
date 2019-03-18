from app.parser import match

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
def test__match_recognized_digits(_input, expected_output):
  schema = match('\n'.join(_input))
  assert schema.value() == expected_output


@pytest.mark.parametrize('_input', [
  (' _ ',
   '|  ',
   ' _ ',
  ),
  (' _ ',
   ' _ ',
   '  |',
  ),
  ('   ',
   '| |',
   '| |',
  ),
  ('   ',
   ' _|',
   '| |',
  ),
])
def test__match_unrecognized_digit(_input):
  schema = match('\n'.join(_input))
  assert schema.value() == '?'

@pytest.mark.parametrize('_input, first_match, optional', [
  ((
    ' _ ',
    '|  ',
    '|_|'
  ), '0', ['6']),
  ((
    ' _ ',
    ' _ ',
    ' _|'
  ), '3', ['5']),
  ((
    '   ',
    '   ',
    '  |'
  ), '1', []),
  ((
    '   ',
    '|_|',
    '   '
  ), '4', []),
  ((
    ' _ ',
    '|_ ',
    ' _|'
  ), '5', ['6', '9'])
])
def test__match_lookalike_digits(_input, first_match, optional):
  schema = match('\n'.join(_input))
  assert schema.value() == first_match

  for digit, expected in zip(schema.close_digits(), optional):
    assert digit.value == expected
