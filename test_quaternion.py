import pytest
from quaternion import Quaternion
import math

def test_initialization():
    q = Quaternion(1, 2, 3, 4)
    assert q.w == 1
    assert q.x == 2
    assert q.y == 3
    assert q.z == 4

def test_addition():
    q1 = Quaternion(1, 2, 3, 4)
    q2 = Quaternion(4, 3, 2, 1)
    result = q1 + q2
    assert result == Quaternion(5, 5, 5, 5)

def test_subtraction():
    q1 = Quaternion(5, 7, 9, 11)
    q2 = Quaternion(1, 2, 3, 4)
    result = q1 - q2
    assert result == Quaternion(4, 5, 6, 7)

def test_multiplication():
    q1 = Quaternion(1, 2, 3, 4)
    q2 = Quaternion(5, 6, 7, 8)
    result = q1 * q2
    assert result == Quaternion(-60, 12, 30, 24)

def test_absolute_value():
    q = Quaternion(1, 2, 3, 4)
    assert math.isclose(abs(q), 5.4772, rel_tol=1e-4)

def test_conjugate():
    q = Quaternion(1, 2, 3, 4)
    result = q.conjugate()
    assert result == Quaternion(1, -2, -3, -4)

def test_inverse():
    q = Quaternion(1, 2, 3, 4)
    result = q.inverse()
    expected_mod_squared = 30
    assert result == Quaternion(1/expected_mod_squared, -2/expected_mod_squared, -3/expected_mod_squared, -4/expected_mod_squared)

def test_division():
    q1 = Quaternion(1, 2, 3, 4)
    q2 = Quaternion(5, 6, 7, 8)
    result = q1 / q2
    expected = q1 * q2.inverse()
    assert result == expected

def test_rotate_vector():
    q = Quaternion(0, 1, 0, 0)  # 180-degree rotation around x-axis
    vector = (0, 1, 0)
    result = q.rotate_vector(vector)
    assert result == (0, -1, 0)

def test_repr():
    q = Quaternion(1, 2, 3, 4)
    assert repr(q) == "Quaternion(1, 2, 3, 4)"

if __name__ == "__main__":
    pytest.main()
