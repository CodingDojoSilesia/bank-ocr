from ocr import scan


def test_input_0s():
    input_ = (
        " _  _  _  _  _  _  _  _  _ \n"
        "| || || || || || || || || |\n"
        "|_||_||_||_||_||_||_||_||_|\n"
        "                           "
    )
    assert scan(input_) == "000000000"


def test_input_1s():
    input_ = (
        "                           \n"
        "  |  |  |  |  |  |  |  |  |\n"
        "  |  |  |  |  |  |  |  |  |\n"
        "                           "
    )
    assert scan(input_) == "111111111"


def test_input_2s():
    input_ = (
        " _  _  _  _  _  _  _  _  _ \n"
        " _| _| _| _| _| _| _| _| _|\n"
        "|_ |_ |_ |_ |_ |_ |_ |_ |_ \n"
        "                           "
    )
    assert scan(input_) == "222222222"


def test_input_3s():
    input_ = (
        " _  _  _  _  _  _  _  _  _ \n"
        " _| _| _| _| _| _| _| _| _|\n"
        " _| _| _| _| _| _| _| _| _|\n"
        "                          "
    )
    assert scan(input_) == "333333333"


def test_input_4s():
    input_ = (
        "                           \n"
        "|_||_||_||_||_||_||_||_||_|\n"
        "  |  |  |  |  |  |  |  |  |\n"
        "                           "
    )
    assert scan(input_) == "444444444"


def test_input_5s():
    input_ = (
        " _  _  _  _  _  _  _  _  _ \n"
        "|_ |_ |_ |_ |_ |_ |_ |_ |_ \n"
        " _| _| _| _| _| _| _| _| _|\n"
        "                           "
    )
    assert scan(input_) == "555555555"


def test_input_6s():
    input_ = (
        " _  _  _  _  _  _  _  _  _ \n"
        "|_ |_ |_ |_ |_ |_ |_ |_ |_ \n"
        "|_||_||_||_||_||_||_||_||_|\n"
        "                           "
    )
    assert scan(input_) == "666666666"


def test_input_7s():
    input_ = (
        " _  _  _  _  _  _  _  _  _ \n"
        "  |  |  |  |  |  |  |  |  |\n"
        "  |  |  |  |  |  |  |  |  |\n"
        "                           "
    )
    assert scan(input_) == "777777777"


def test_input_8s():
    input_ = (
        " _  _  _  _  _  _  _  _  _ \n"
        "|_||_||_||_||_||_||_||_||_|\n"
        "|_||_||_||_||_||_||_||_||_|\n"
        "                           "
    )
    assert scan(input_) == "888888888"


def test_input_9s():
    input_ = (
        " _  _  _  _  _  _  _  _  _ \n"
        "|_||_||_||_||_||_||_||_||_|\n"
        " _| _| _| _| _| _| _| _| _|\n"
        "                           "
    )
    assert scan(input_) == "999999999"


def test_input_123456789():
    input_ = (
        "    _  _     _  _  _  _  _ \n"
        "  | _| _||_||_ |_   ||_||_|\n"
        "  ||_  _|  | _||_|  ||_| _|\n"
        "                           "
    )
    assert scan(input_) == "123456789"


def test_input_000000051():
    input_ = (
        " _  _  _  _  _  _  _  _    \n"
        "| || || || || || || ||_   |\n"
        "|_||_||_||_||_||_||_| _|  |\n"
        "                           "
    )
    assert scan(input_) == "000000051"


def test_input_49006771_ill():
    input_ = (
        "    _  _  _  _  _  _     _ \n"
        "|_||_|| || ||_   |  |  | _ \n"
        "  | _||_||_||_|  |  |  | _|\n"
        "                           "
    )
    assert scan(input_) == "49006771? ILL"


def test_input_12345678_ill():
    input_ = (
        "    _  _     _  _  _  _  _ \n"
        "  | _| _||_| _ |_   ||_||_|\n"
        "  ||_  _|  | _||_|  ||_| _ \n"
        "                           "
    )
    assert scan(input_) == "1234?678? ILL"


import ocr

input_valid = (
    " _  _  _  _  _  _  _  _  _ \n"
    "| || || || || || || || || |\n"
    "|_||_||_||_||_||_||_||_||_|\n"
    "                           "
)

valid_number = ocr.Number(input_valid)

input_invalid = (
        "    _  _     _  _  _  _  _ \n"
        "  | _| _||_| _ |_   ||_||_|\n"
        "  ||_  _|  | _||_|  ||_| _ \n"
        "                           "
    )
invalid_number = ocr.Number(input_invalid)
