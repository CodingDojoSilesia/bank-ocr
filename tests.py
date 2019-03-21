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


def test_input_7s():
    input_ = (
        " _  _  _  _  _  _  _  _  _ \n"
        "  |  |  |  |  |  |  |  |  |\n"
        "  |  |  |  |  |  |  |  |  |\n"
        "                           "
    )
    assert scan(input_) == "777777777"


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


def test_guessed_333333333():
    input_ = (
        " _  _  _  _  _  _  _  _  _ \n"
        " _| _| _| _| _| _| _| _| _|\n"
        " _| _| _| _| _| _| _| _| _|\n"
        "                          "
    )
    assert guessed_scan(input_) == "333393333"



def test_guessed_999999999():
    input_ = (
        " _  _  _  _  _  _  _  _  _ \n"
        "|_||_||_||_||_||_||_||_||_|\n"
        " _| _| _| _| _| _| _| _| _|\n"
        "                           "
    )
    assert (
        guessed_scan(input_) == "999999999 AMB ['899999999', '993999999', '999959999']"
    )


def test_guessed_490067715():
    input_ = (
        "    _  _  _  _  _  _     _ \n"
        "|_||_|| || ||_   |  |  ||_ \n"
        "  | _||_||_||_|  |  |  | _|\n"
        "                           "
    )
    assert (
        guessed_scan(input_) == "490067715 AMB ['490067115', '490067719', '490867715']"
    )


def test_guessed_123456789():
    input_ = (
        "    _  _     _  _  _  _  _ \n"
        " _| _| _||_||_ |_   ||_||_|\n"
        "  ||_  _|  | _||_|  ||_| _|\n"
        "                           "
    )
    assert guessed_scan(input_) == "123456789"
