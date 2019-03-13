from app.parser import ExactDigitParser, FuzzyDigitParser
from app.reader import AccountNumberFileReader, AccountNumberLineReader
from app.validator import is_valid, is_error

INVALID = 'ILL'
ERROR = 'ERR'
FNAME = '/src/app/data.in'


def story_01():
  print('''
    ######################
    #### USER STORY 1 ####
    ######################''')
  file_reader = AccountNumberFileReader(FNAME)
  parser = ExactDigitParser()

  for line in file_reader.read():
    line_reader = AccountNumberLineReader(line)
    print(line)
    digits = list(map(parser.parse, line_reader.read()))
    print('=>', ''.join(digits))


def story_02():
  print('''
    #######################
    #### USER STORY 2+3 ###
    #######################''')
  file_reader = AccountNumberFileReader(FNAME)
  parser = ExactDigitParser()

  for line in file_reader.read():
    line_reader = AccountNumberLineReader(line)
    print(line)
    digits = list(map(parser.parse, line_reader.read()))
    if is_error(digits):
      print('=>', ''.join(digits), ERROR)
    elif not is_valid(digits):
      print('=>', ''.join(digits), INVALID)
    else:
      print('=>', ''.join(digits))


if __name__ == '__main__':
  story_01()
  story_02()