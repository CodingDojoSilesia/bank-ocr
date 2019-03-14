from ocr import scan, validated_scan, guessed_scan


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


def test_validation_000000051():
    input_ = (
        " _  _  _  _  _  _  _  _    \n"
        "| || || || || || || ||_   |\n"
        "|_||_||_||_||_||_||_| _|  |\n"
        "                           "
    )
    assert validated_scan(input_) == "000000051"


def test_validation_49006771_ill():
    input_ = (
        "    _  _  _  _  _  _     _ \n"
        "|_||_|| || ||_   |  |  | _ \n"
        "  | _||_||_||_|  |  |  | _|\n"
        "                           "
    )
    assert validated_scan(input_) == "49006771? ILL"


def test_validation_12345678_ill():
    input_ = (
        "    _  _     _  _  _  _  _ \n"
        "  | _| _||_| _ |_   ||_||_|\n"
        "  ||_  _|  | _||_|  ||_| _ \n"
        "                           "
    )
    assert validated_scan(input_) == "1234?678? ILL"


def test_validation_664371495_err():
    input_ = (
        " _  _     _  _        _  _ \n"
        "|_ |_ |_| _|  |  ||_||_||_ \n"
        "|_||_|  | _|  |  |  | _| _|\n"
        "                           "
    )
    assert validated_scan(input_) == "664371495 ERR"


def test_guessed_111111111():
    input_ = (
        "                           \n"
        "  |  |  |  |  |  |  |  |  |\n"
        "  |  |  |  |  |  |  |  |  |\n"
        "                           "
    )
    assert guessed_scan(input_) == "711111111"


def test_guessed_777777777():
    input_ = (
        " _  _  _  _  _  _  _  _  _ \n"
        "  |  |  |  |  |  |  |  |  |\n"
        "  |  |  |  |  |  |  |  |  |\n"
        "                           "
    )
    assert guessed_scan(input_) == "777777177"


def test_guessed_200000000():
    input_ = (
        " _  _  _  _  _  _  _  _  _ \n"
        " _|| || || || || || || || |\n"
        "|_ |_||_||_||_||_||_||_||_|\n"
        "                           "
    )
    assert guessed_scan(input_) == "200800000"


def test_guessed_333333333():
    input_ = (
        " _  _  _  _  _  _  _  _  _ \n"
        " _| _| _| _| _| _| _| _| _|\n"
        " _| _| _| _| _| _| _| _| _|\n"
        "                          "
    )
    assert guessed_scan(input_) == "333393333"


def test_guessed_888888888():
    input_ = (
        " _  _  _  _  _  _  _  _  _ \n"
        "|_||_||_||_||_||_||_||_||_|\n"
        "|_||_||_||_||_||_||_||_||_|\n"
        "                           "
    )
    assert guessed_scan(input_) == "888888888 AMB ['888886888', '888888880', '888888988']"


def test_guessed_555555555():
    input_ = (
        " _  _  _  _  _  _  _  _  _ \n"
        "|_ |_ |_ |_ |_ |_ |_ |_ |_ \n"
        " _| _| _| _| _| _| _| _| _|\n"
        "                           "
    )
    assert guessed_scan(input_) == "555555555 AMB ['555655555', '559555555']"


def test_guessed_666666666():
    input_ = (
        " _  _  _  _  _  _  _  _  _ \n"
        "|_ |_ |_ |_ |_ |_ |_ |_ |_ \n"
        "|_||_||_||_||_||_||_||_||_|\n"
        "                           "
    )
    assert guessed_scan(input_) == "666666666 AMB ['666566666', '686666666']"


def test_guessed_999999999():
    input_ = (
        " _  _  _  _  _  _  _  _  _ \n"
        "|_||_||_||_||_||_||_||_||_|\n"
        " _| _| _| _| _| _| _| _| _|\n"
        "                           "
    )
    assert guessed_scan(input_) == "999999999 AMB ['899999999', '993999999', '999959999']"


def test_guessed_490067715():
    input_ = (
        "    _  _  _  _  _  _     _ \n"
        "|_||_|| || ||_   |  |  ||_ \n"
        "  | _||_||_||_|  |  |  | _|\n"
        "                           "
    )
    assert guessed_scan(input_) == "490067715 AMB ['490067115', '490067719', '490867715']"


def test_guessed_123456789():
    input_ = (
        "    _  _     _  _  _  _  _ \n"
        " _| _| _||_||_ |_   ||_||_|\n"
        "  ||_  _|  | _||_|  ||_| _|\n"
        "                           "
    )
    assert guessed_scan(input_) == "123456789"


def test_guessed_000000051():
    input_ = (
        " _     _  _  _  _  _  _    \n"
        "| || || || || || || ||_   |\n"
        "|_||_||_||_||_||_||_| _|  |\n"
        "                           "
    )
    assert guessed_scan(input_) == "000000051"


def test_guessed_490867715():
    input_ = (
        "    _  _  _  _  _  _     _ \n"
        "|_||_|| ||_||_   |  |  | _ \n"
        "  | _||_||_||_|  |  |  | _|\n"
        "                           "
    )
    assert guessed_scan(input_) == "490867715"


import ocr

input_valid = (
    " _  _  _  _  _  _  _  _  _ \n"
    "| || || || || || || || || |\n"
    "|_||_||_||_||_||_||_||_||_|\n"
    "                           "
)

valid_number = ocr.Number.from_text(input_valid)
input_invalid = (
    "    _  _     _  _  _  _  _ \n"
    "  | _| _||_| _ |_   ||_||_|\n"
    "  ||_  _|  | _||_|  ||_| _ \n"
    "                           "
)
invalid_number = ocr.Number.from_text(input_invalid)
