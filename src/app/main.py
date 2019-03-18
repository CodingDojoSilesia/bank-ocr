from app.reader import AccountNumberFileReader, AccountNumberLineReader
from app.parser import match
from app.number import AccountNumber, Digit, UnknownDigit
from app.tools import AccountNumberGenerator


AMB = 'AMB'
ILL = 'ILL'
ERR = 'ERR'
case_04 = '/src/app/usecase04.in'
fname = '/src/app/data.in'

file_reader = AccountNumberFileReader()
line_reader = AccountNumberLineReader()

def story_01():
  print('''
    ######################
    #### USER STORY 1 ####
    ######################''')

  for line in file_reader.readlines(fname):
    number = line_reader.read_digits(line)
    schemas = [match(n) for n in number]
    account = AccountNumber([s.digit for s in schemas])
    print('=>', account)

def story_02():
  print('''
    #######################
    #### USER STORY 2+3 ###
    #######################''')

  for line in file_reader.readlines(fname):
    number = line_reader.read_digits(line)
    schemas = [match(n) for n in number]
    account = AccountNumber([s.digit for s in schemas])
    if account.is_malformed():
      print('=>', account, ILL)
    elif account.is_error():
      print('=>', account, ERR)
    else:
      print('=>', account)


def story_04():
  print('''
    #######################
    #### USER STORY 4 ####
    #######################''')

  for line in file_reader.readlines(case_04):
    number = line_reader.read_digits(line)
    schemas = [match(n) for n in number]
    account = AccountNumber([s.digit for s in schemas])
    if not account.is_malformed() and not account.is_error():
      print('=>', account)
    else:
      account_generator = AccountNumberGenerator(schemas)
      accounts = [acc for acc in account_generator if not acc.is_malformed()]
      valid_accounts = [acc for acc in accounts if not acc.is_error()]
      if not valid_accounts:
        print('=>', account, ILL)
      elif len(valid_accounts) > 1:
        print('=>', account, AMB, list(map(str, valid_accounts)))
      else:
        print('=>', valid_accounts[0])

if __name__ == '__main__':
  story_01()
  story_02()
  story_04()
