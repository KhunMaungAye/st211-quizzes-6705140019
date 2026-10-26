from unittest.mock import Mock

def test_mock_basics():
    mock = Mock()

    result = mock.whatever(1, 2, 3)
    print(result)
    assert isinstance(result, Mock)
