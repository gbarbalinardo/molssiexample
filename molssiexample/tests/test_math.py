import molssiexample as me
import pytest


@pytest.mark.parametrize('n, answer', [(0, 1), (1, 2), (2, 2.5), (3, 2.666)])
def test_euler(n, answer):
    assert me.math.euler(n) == pytest.approx(answer, abs=3)


def test_euler_failure():
    with pytest.raises(ValueError) as exc:
        me.math.euler(-1)
    assert "positive int" in str(exc.value)

@pytest.mark.parametrize('n, answer', [(1000, 3.1)])
def test_euler(n, answer):
    assert me.math.pi(n) == pytest.approx(answer, abs=2)

