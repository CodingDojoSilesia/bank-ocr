from app.reader import AccountNumberFileReader, AccountNumberLineReader
from app.parser import match
from app.number import AccountNumber, Digit, UnknownDigit
from app.tools import AccountNumberGenerator
from app.scanner import scan, guess_scan


fname = '/src/app/data.in'

file_reader = AccountNumberFileReader()

def story_01_02_03():
  print('''
    #########################
    #### USER STORY 1+2+3 ###
    #########################''')

  for line in file_reader.readlines(fname):
    print('=>', scan(line))
    


def story_04():
  print('''
    #######################
    #### USER STORY 4 ####
    #######################''')

  for line in file_reader.readlines(fname):
    print('=>', guess_scan(line))

if __name__ == '__main__':
  story_01_02_03()
  story_04()
