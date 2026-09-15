import pytest

from validators import validate_email, validate_age


def test_invalid_email():
    with pytest.raises(ValueError):
        validate_email("invalid-email")


def test_invalid_email_without_domain():
    with pytest.raises(ValueError):
        validate_email("testing@")


def test_invalid_age():
    with pytest.raises(ValueError):
        validate_age(-1)


def test_age_too_high():
    with pytest.raises(ValueError):
        validate_age(151)


def test_valid_type_age():
    with pytest.raises(ValueError):
        validate_age("one")
