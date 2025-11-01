from routers import classification_consulting


def test_valid_old_plate():
    assert classification_consulting.is_valid_plate("ABC-1234")

def test_valid_mercosul_plate():
    assert classification_consulting.is_valid_plate("ABC1D23")

def test_invalid_format_letters():
    assert not classification_consulting.is_valid_plate("ABCD123")

def test_invalid_format_numbers():
    assert not classification_consulting.is_valid_plate("ABC-123")

def test_invalid_structure():
    assert not classification_consulting.is_valid_plate("A1C2D34")
