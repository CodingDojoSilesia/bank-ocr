from app.strategies import ExactMatching, FuzzyMatching

class DigitParser(object):
  NOT_FOUND = '?'
  
  def __init__(self, match_strategy):
    self.strategy = match_strategy

  def parse(self, digit):
    match = self.strategy.match(digit)
    return match or self.NOT_FOUND

class ExactDigitParser(DigitParser):
  def __init__(self):
    super().__init__(match_strategy=ExactMatching())

class FuzzyDigitParser(DigitParser):
  def __init__(self):
    super().__init__(match_strategy=FuzzyMatching())
