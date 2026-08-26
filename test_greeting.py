import pytest

from greeting import greet


def test_greet() -> None:
    assert greet("Ada") == "Hello, Ada!"


def test_greet_normalizes_whitespace() -> None:
    assert greet("  Ada  ") == "Hello, Ada!"


def test_greet_normalizes_internal_whitespace() -> None:
    assert greet("  Ada   Lovelace  ") == "Hello, Ada Lovelace!"


def test_greet_rejects_empty_input() -> None:
    with pytest.raises(ValueError):
        greet("   ")


def test_greet_rejects_null() -> None:
    with pytest.raises(ValueError):
        greet(None)


def test_greet_rejects_non_string() -> None:
    with pytest.raises(TypeError):
        greet(123)
