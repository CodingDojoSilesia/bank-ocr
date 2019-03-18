from typing import List

from app.number import Digit, UnknownDigit, DigitSchema
from app.settings import KNOWN_SCHEMAS, unknown


def _match_exact(text: str) -> DigitSchema:
  target_schema = text.split('\n')
  for schema in KNOWN_SCHEMAS:
    diff_count = schema.count_differences(target_schema)
    if diff_count == 0:
      return schema
  return None

def _match_close(text: str, diff_limit: int = 1) -> DigitSchema:
  target_schema = text.split('\n')
  possible_digits = []
  for schema in KNOWN_SCHEMAS:
    diff_count = schema.count_differences(target_schema)
    if 0 < diff_count <= diff_limit:
      possible_digits.append(schema.digit)  
  if possible_digits:
    return DigitSchema(
      schema=target_schema,
      digit=possible_digits[0],
      optional=possible_digits[1:]
    )
  return None

def match(text: str) -> DigitSchema:
  match = _match_exact(text)
  if not match:
    match = _match_close(text)
  return match or DigitSchema(
    schema=text,
    digit=UnknownDigit(),
    optional=[]
  )
