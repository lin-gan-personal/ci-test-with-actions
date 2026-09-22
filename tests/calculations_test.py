# System Modules
import sys
import os

# Installed Modules
import pytest

# Project Modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from calculations import area_of_circle, generate_two_random_reals, get_nth_fibonacci  # noqa: E402


def test_area_of_circle_positive_radius():
    """Test with a positive radius."""
    # Arrange
    radius = 1

    # Act
    result = area_of_circle(radius)

    # Assert
    assert abs(result - 3.14159) < 1e-5


def test_area_of_circle_zero_radius():
    """Test with a radius of zero."""
    # Arrange
    radius = 0

    # Act
    result = area_of_circle(radius)

    # Assert
    assert result == 0


def test_get_nth_fibonacci_zero():
    """Test with n=0."""
    # Arrange
    n = 0

    # Act
    result = get_nth_fibonacci(n)

    # Assert
    assert result == 0


def test_get_nth_fibonacci_one():
    """Test with n=1."""
    # Arrange
    n = 1

    # Act
    result = get_nth_fibonacci(n)

    # Assert
    assert result == 1


def test_get_nth_fibonacci_ten():
    """Test with n=10."""
    # Arrange
    n = 10
    # Act
    result = get_nth_fibonacci(n)

    # Assert
    assert result == 55


def test_area_of_circle_negative_radius_raises_value_error():
    """Test negative radius raises ValueError."""
    # Arrange
    radius = -1

    # Act / Assert
    with pytest.raises(ValueError, match="Radius cannot be negative"):
        area_of_circle(radius)


def test_get_nth_fibonacci_negative_raises_value_error():
    """Test negative n raises ValueError."""
    # Arrange
    n = -1

    # Act / Assert
    with pytest.raises(ValueError, match="n cannot be negative"):
        get_nth_fibonacci(n)


def test_generate_two_random_reals_default_range(monkeypatch):
    """Test default range produces two floats in [0.0, 1.0]."""
    values = iter([0.1, 0.9])
    calls = []

    def fake_uniform(min_val, max_val):
        calls.append((min_val, max_val))
        return next(values)

    monkeypatch.setattr("random.uniform", fake_uniform)

    result = generate_two_random_reals()

    assert result == (0.1, 0.9)
    assert calls == [(0.0, 1.0), (0.0, 1.0)]


def test_generate_two_random_reals_custom_range(monkeypatch):
    """Test custom range uses the provided bounds."""
    values = iter([2.5, 3.5])
    calls = []

    def fake_uniform(min_val, max_val):
        calls.append((min_val, max_val))
        return next(values)

    monkeypatch.setattr("random.uniform", fake_uniform)

    result = generate_two_random_reals(min_val=2.0, max_val=4.0)

    assert result == (2.5, 3.5)
    assert calls == [(2.0, 4.0), (2.0, 4.0)]
