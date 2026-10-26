from unittest.mock import Mock
import pytest

def test_comparison():
    mock = Mock()

    mock.fetch.side_effect = RuntimeError("Boom")
    mock.fetch.return_value = "Success"

    # with pytest.raises(RuntimeError):
    #     mock.fetch()

    mock.fetch.side_effect = None

    assert mock.fetch() == "Success"

    