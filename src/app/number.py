from typing import List


class Digit(object):
  def __init__(self, value: str):
    self.value = value

  def __str__(self):
    return self.value

  def __eq__(self, value):
    return self.value == value

class UnknownDigit(Digit):
  CHAR = '?'
  def __init__(self):
    super().__init__(self.CHAR)


class DigitSchema(Digit):
  def __init__(self, schema: List[str], digit: Digit, optional: List[Digit]):
    self.schema = schema
    self.digit = digit
    self.optional = optional

  def close_digits(self) -> List[Digit]:
    return self.optional

  def value(self) -> str:
    return self.digit.value

  def count_differences(self, target: List[str]) -> int:
    return sum((self.schema[r][c] != target[r][c] for r in range(3) 
                                                  for c in range(3)))

  def __str__(self):
    return self.value()

class AccountNumber(object):
  def __init__(self, digits: List[Digit]):
    self.digits = digits

  def is_error(self) -> bool:
    summary = 0
    for multiplayer, digit in enumerate(self.digits[::-1], 1):
      summary += int(digit.value) * multiplayer
    return summary % 11 != 0

  def is_malformed(self) -> bool:
    return any((d.value == UnknownDigit.CHAR for d in self.digits))

  def __str__(self):
    return ''.join(map(str, self.digits))
