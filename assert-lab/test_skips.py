import pytest
import sys

@pytest.mark.skip(reason= "Feature not implemented yet")
def test_future_feature():
    assert False

@pytest.mark.skipif(sys.version_info < (3, 8), reason = "Required Python 3.8+")
def test_needs_morden_python():
    assert True