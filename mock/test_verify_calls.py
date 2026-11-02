from unittest.mock import Mock

def test_was_called():
    mock = Mock()
    mock.save()
    mock.save()
    mock.save.assert_called()

def test_was_called_once():
    mock = Mock()
    mock.save()
    mock.save.assert_called_once()
