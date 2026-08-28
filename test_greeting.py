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


def test_greet_normalizes_tabs_and_newlines() -> None:
    assert greet("  Ada\t Lovelace\n") == "Hello, Ada Lovelace!"


def test_greet_rejects_empty_string() -> None:
    with pytest.raises(ValueError):
        greet("")


def test_greet_rejects_null_with_message() -> None:
    with pytest.raises(ValueError, match="name must not be null"):
        greet(None)


@pytest.mark.parametrize(
    "invalid",
    [3.14, b"Ada", ["Ada"], {"name": "Ada"}],
)
def test_greet_rejects_other_non_string_types(invalid: object) -> None:
    with pytest.raises(TypeError):
        greet(invalid)


def test_greet_rejects_whitespace_only_tabs_and_newlines() -> None:
    with pytest.raises(ValueError):
        greet("\t\n  ")


def test_greet_rejects_boolean_as_non_string() -> None:
    with pytest.raises(TypeError):
        greet(True)


def test_greet_normalizes_newline_within_name() -> None:
    assert greet("Ada\nLovelace") == "Hello, Ada Lovelace!"


def test_greet_normalizes_tab_within_name() -> None:
    assert greet("Grace\tHopper") == "Hello, Grace Hopper!"
