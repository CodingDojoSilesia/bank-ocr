from app.strategies import ExactMatching, FuzzyMatching


class DigitParserFactory(object):
  NOT_FOUND = '?'

  def __init__(self, strategy):
    self.strategy = strategy

  def parse(self, digit):
    return self.strategy.parse(digit) or self.NOT_FOUND
  
ExactDigitParser = DigitParserFactory(ExactMatching())
FuzzyDigitParser = DigitParserFactory(FuzzyMatching())
