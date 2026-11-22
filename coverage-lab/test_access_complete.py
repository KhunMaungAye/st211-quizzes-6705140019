from access import check_access

def test_admin_active_granted():
    assert check_access("admin", True) == "granted"

def test_non_admin_inactive_denied():
    assert check_access("user", False) == "denied"

def test_admin_inactive_denied():
    assert check_access("admin", False) == "denied"

def test_non_admin_active_denied():
    assert check_access("user", True) == "denied"