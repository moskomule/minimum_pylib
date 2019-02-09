from foo import cum_add
import pytest


def test_cum_add():
    assert cum_add(1, 2, 3, 4, 5) == 15
    assert cum_add("x", "y", "z") == "xyz"
    with pytest.raises(TypeError):
        cum_add(1, "2", 3)
