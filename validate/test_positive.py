from validators import validate_email, validate_age


def test_valid_email():
    assert validate_email("test@example.com") is True


def test_valid_age():
    assert validate_age(22) is True


def test_boundary_ages_accepted():
    assert validate_age(0) is True
    assert validate_age(150) is True
