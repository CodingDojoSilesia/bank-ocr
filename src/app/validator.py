def is_valid(number):
  summary = 0
  for multiplayer, digit in enumerate(number[::-1], 1):
    summary += int(digit) * multiplayer
  return summary % 11 == 0

def is_error(number):
  return '?' in number
