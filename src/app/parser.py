from typing import List

from app.number import Digit, UnknownDigit, DigitSchema
from app.settings import KNOWN_SCHEMAS, unknown


def _match(text: str, diff_limit: int = 1) -> DigitSchema:
  target_schema = text.split('\n')
  possible_matches = []
  for schema in KNOWN_SCHEMAS:
    if schema.matches(target_schema):
      return schema
    elif schema.matches(target_schema, diff_limit=diff_limit):
      possible_matches.append(schema.digit)
  
  if possible_matches:
    return DigitSchema(
      schema=target_schema,
      digit=possible_matches[0],
      optional=possible_matches[1:]
    )
  return None

def match(text: str) -> DigitSchema:
  return _match(text) or DigitSchema(
    schema=text,
    digit=UnknownDigit(),
    optional=[]
  )
