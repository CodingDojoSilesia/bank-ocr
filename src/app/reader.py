class AccountNumberFileReader(object):
  def __init__(self, fname):
    self.fname = fname

  def read(self):
    with open(self.fname, 'r') as fp:
      while True:
        try:
          yield next(fp) + next(fp) + next(fp)
        except StopIteration:
          break


class AccountNumberLineReader(object):
  def __init__(self, line):
    self.line = line
    self.digits = 9

  
  def _get_nth_number(self, n):
    rows = self.line.split('\n')
    return '\n'.join((
      rows[0][n * 3: (n * 3) + 3],
      rows[1][n * 3: (n * 3) + 3],
      rows[2][n * 3: (n * 3) + 3],
    ))

  def read(self, digits=9):
    for n in range(digits):
      yield self._get_nth_number(n)
