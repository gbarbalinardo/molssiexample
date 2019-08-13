import molssiexample as me
import pytest


@pytest.mark.parametrize('n, answer', [(0, 1), (1, 2), (2, 2.5)])
def test_euler(n, answer):
    assert me.math.euler(n) == answer