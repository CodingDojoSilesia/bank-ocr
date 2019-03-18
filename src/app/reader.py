class AccountNumberFileReader(object):
  def readlines(self, fname):
    with open(fname, 'r') as fp:
      while True:
        try:
          yield next(fp) + next(fp) + next(fp)
        except StopIteration:
          break


class AccountNumberLineReader(object):  
  def _get_nth_number(self, n, line):
    rows = line.split('\n')
    return '\n'.join((
      rows[0][n * 3: (n * 3) + 3],
      rows[1][n * 3: (n * 3) + 3],
      rows[2][n * 3: (n * 3) + 3],
    ))

  def read_digits(self, line, digits=9):
    for n in range(digits):
      yield self._get_nth_number(n, line)
