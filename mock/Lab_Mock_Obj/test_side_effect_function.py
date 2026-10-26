from unittest.mock import Mock

def double(x):
    return x * 3

def test_side_effect_function(): #side effect can execute a real function whatever mock call and return the actual result
    mock = Mock()

    mock.calculate.return_value = 10

    assert mock.calculate(5) == 10