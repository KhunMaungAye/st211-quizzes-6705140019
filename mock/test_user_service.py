from unittest.mock import Mock

from mock.user_service import UserService

def test_get_username():
    db = Mock()
    db.find_user.return_value = "Alice"

    service = UserService(db)

    assert service.get_username(1) == "Alice"
    