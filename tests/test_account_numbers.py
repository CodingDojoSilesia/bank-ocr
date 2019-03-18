import pytest

from app.settings import *
from app.number import UnknownDigit, AccountNumber


def _to_digits(number):
  mapping = {
    '0': zero,
    '1': one,
    '2': two,
    '3': three,
    '4': four,
    '5': five,
    '6': six,
    '7': seven,
    '8': eight,
    '9': nine,
    '?': UnknownDigit(),
  }
  return list(map(mapping.get, number))


@pytest.mark.parametrize('number, expected',(
('123456789', False),
('490067715', True),
('666666666', True),
('000000051', False),
('000000057', True),
))
def test_account_number_error_validation(number, expected):
  digits = _to_digits(number)
  assert AccountNumber(digits).is_error() == expected


@pytest.mark.parametrize('number, expected',(
('123456789', False),
('49006?715', True),
('666??6666', True),
('000000051', False),
('00000005?', True),
))
def test_account_number_malform_detection(number, expected):
  digits = _to_digits(number)
  assert AccountNumber(digits).is_malformed() == expected
