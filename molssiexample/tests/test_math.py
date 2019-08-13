import molssiexample as me
import pytest
import numpy as np

@pytest.mark.parametrize('n, answer', [(0, 1), (1, 2), (2, 2.5), (3, 2.666)])
def test_euler(n, answer):
    assert me.math.euler(n) == pytest.approx(answer, abs=3)


def test_euler_failure():
    with pytest.raises(ValueError) as exc:
        me.math.euler(-1)
    assert "positive int" in str(exc.value)


def test_pi():
    np.random.seed(0)
    assert me.math.pi(1e7) == pytest.approx(3.141, abs=1.e-3)