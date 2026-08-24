import pytest

from greeting import greet


def test_greet() -> None:
    assert greet("Ada") == "Hello, Ada!"


def test_greet_normalizes_whitespace() -> None:
    assert greet("  Ada  ") == "Hello, Ada!"


def test_greet_rejects_empty_input() -> None:
    with pytest.raises(ValueError):
        greet("   ")
