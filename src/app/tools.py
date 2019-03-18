from typing import List, Iterable

from app.number import DigitSchema, AccountNumber


class AccountNumberGenerator(object):  
  def __init__(self, schemas: List[DigitSchema]):
    self.schemas = schemas

  def __iter__(self):
    return self.generate()

  def generate(self) -> Iterable[AccountNumber]:
    '''
      Generate possible account numbers from given schemas
      allowing to change one digit at a time
    '''
    schemas = self.schemas
    for i in range(len(schemas)):
      left = [schema.digit for schema in schemas[:i]]
      schema = schemas[i]
      right = [schema.digit for schema in schemas[i + 1:]]
      for digit in schema.close_digits():
        yield AccountNumber(left + [digit] + right)
