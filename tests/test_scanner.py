import pytest

from app.scanner import scan, guess_scan
from app.reader import AccountNumberFileReader

TEST_FILE = '/src/app/data.in'

SCAN_EXPECTED = [
  "123456789",
  "490067715 ERR",
  "666666666 ERR",
  "000000051",
  "000000057 ERR",
  "128436789 ERR",
  "450037715 ERR",
  "1??7??7?? ILL",
  "490067715 ERR",
  "123456781 ERR",
  "604371495 ERR",
]

GUESS_SCAN_EXPECTED = [
  "123456789",
  "490067715 AMB ['490867715', '490067115', '490067719']",
  "666666666 AMB ['686666666', '666566666']",
  "000000051",
  "000000051",
  "128436789 AMB ['126436789', '128438789']",
  "450037715 ERR",
  "1??7??7?? ILL",
  "490067715 AMB ['490867715', '490067115', '490067719']",
  "123458781",
  "604371495 AMB ['504371495', '604377495']",
]

def test_scan():
  reader = AccountNumberFileReader()
  for line, expected in zip(reader.readlines(TEST_FILE), SCAN_EXPECTED):
    assert scan(line) == expected

def test_guess_scan():
  reader = AccountNumberFileReader()
  for line, expected in zip(reader.readlines(TEST_FILE), GUESS_SCAN_EXPECTED):
    assert guess_scan(line) == expected