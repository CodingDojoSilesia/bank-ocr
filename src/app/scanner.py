from typing import List, Tuple

from app.number import DigitSchema, AccountNumber
from app.reader import AccountNumberLineReader
from app.tools import AccountNumberGenerator
from app.parser import match


AMB = 'AMB'
ILL = 'ILL'
ERR = 'ERR'

def scan(number: str) -> str:
  reader = AccountNumberLineReader()
  number = reader.read_digits(number)
  digits = [match(n).digit for n in number]
  acc = AccountNumber(digits)
  if acc.is_malformed():
    return ' '.join((str(acc), ILL))
  elif acc.is_error():
    return ' '.join((str(acc), ERR))
  return str(acc)

def _guess_numbers(schemas: List[DigitSchema]) -> List[AccountNumber]:
  number_generator = AccountNumberGenerator(schemas)
  for number in number_generator:
    if not number.is_malformed() and not number.is_error():
      yield number

def guess_scan(number: str) -> str:
  reader = AccountNumberLineReader()
  number = reader.read_digits(number)
  schemas = [match(n) for n in number]
  digits = [s.digit for s in schemas]
  number = AccountNumber(digits)
  if not number.is_malformed() and not number.is_error():
    return str(number)
  
  valid_numbers = list(_guess_numbers(schemas))
  if not valid_numbers:
    if number.is_malformed():
      return ' '.join((str(number), ILL))
    else:
      return ' '.join((str(number), ERR))
  elif len(valid_numbers) == 1:
    return str(valid_numbers[0])
  else:
    return ' '.join((str(number), AMB, str(list(map(str, valid_numbers)))))
