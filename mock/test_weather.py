import pytest
from unittest.mock import patch

from weather import get_temperature, describe_weather

def test_get_temperature_range():
    temp = get_temperature()

    assert -10 <= temp <= 40

def test_hot_weather():
    with patch("weather.get_temperature", return_value = 30):
        assert describe_weather() == "Hot"

def test_freezing_weather():
    with patch("weather.get_temperature", return_value = -5):
        assert describe_weather() == "Freezing"

@pytest.mark.parametrize("temperature, expected", [
        (-10, "Freezing"),

        (-1, "Freezing"),

        (0, "Cold"),

        (14, "Cold"),

        (15, "Pleasant"),

        (24, "Pleasant"),

        (25, "Hot"),

        (40, "Hot"),
])

def test_describe_weather(temperature, expected):
    with patch("weather.get_temperature", return_value = temperature):
        assert describe_weather() == expected