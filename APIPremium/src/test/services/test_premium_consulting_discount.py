from services.premium_consulting_service import find_discount_by_classification


def test_premium():
    assert find_discount_by_classification("premium") == 100
    assert find_discount_by_classification("PREMIUM") == 100


def test_private():
    assert find_discount_by_classification("private") == 50
    assert find_discount_by_classification("PRIVATE") == 50


def test_basic():
    assert find_discount_by_classification("basic") == 0
    assert find_discount_by_classification("BASIC") == 0


def test_any_other():
    assert find_discount_by_classification("basico") == 0
    assert find_discount_by_classification("not valid") == 0