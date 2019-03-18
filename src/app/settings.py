from app.number import Digit, DigitSchema


unknown = Digit(
  value='?'
)

zero = Digit(
  value='0',
)

one = Digit(
  value='1',
)

two = Digit(
  value='2',
)

three = Digit(
  value='3',
)

four = Digit(
  value='4',
)

five = Digit(
  value='5',
)

six = Digit(
  value='6',
)

seven = Digit(
  value='7',
)

eight = Digit(
  value='8',
)

nine = Digit(
  value='9',
)

zero_schema = DigitSchema(
  schema=(
    ' _ ',
    '| |',
    '|_|',
  ),
  digit=zero,
  optional=[eight]
)

one_schema = DigitSchema(
  schema=(
    '   ',
    '  |',
    '  |'
  ),
  digit=one,
  optional=[seven]
)

two_schema = DigitSchema(
  schema=(
    ' _ ',
    ' _|',
    '|_ '
  ),
  digit=two,
  optional=[six]
)

three_schema = DigitSchema(
  schema=(
    ' _ ',
    ' _|',
    ' _|'
  ),
  digit=three,
  optional=[nine]
)

four_schema = DigitSchema(
  schema=(
    '   ',
    '|_|',
    '  |',
  ),
  digit=four,
  optional=[]
)

five_schema = DigitSchema(
  schema=(
    ' _ ',
    '|_ ',
    ' _|'
  ),
  digit=five,
  optional=[six, nine]
)

six_schema = DigitSchema(
  schema=(
    ' _ ',
    '|_ ',
    '|_|',
  ),
  digit=six,
  optional=[five, eight]
)

seven_schema = DigitSchema(
  schema=(
    ' _ ',
    '  |',
    '  |',
  ),
  digit=seven,
  optional=[one]
)

eight_schema = DigitSchema(
  schema=(
    ' _ ',
    '|_|',
    '|_|',
  ),
  digit=eight,
  optional=[zero, six, nine]
)

nine_schema = DigitSchema(
  schema=(
    ' _ ',
    '|_|',
    ' _|'
  ),
  digit=nine,
  optional=[three, eight]
)

KNOWN_SCHEMAS = [
  zero_schema, one_schema, two_schema,
  three_schema, four_schema, five_schema, 
  six_schema, seven_schema, eight_schema, 
  nine_schema,
]
