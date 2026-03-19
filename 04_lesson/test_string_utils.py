import pytest
from string_utils import StringUtils

utils = StringUtils()

# -------- capitalize --------


def test_capitalize_normal():
    assert utils.capitalize("skypro") == "Skypro"


def test_capitalize_already_capitalized():
    assert utils.capitalize("Skypro") == "Skypro"


def test_capitalize_empty_string():
    # "" — валидная строка, метод должен вернуть ""
    assert utils.capitalize("") == ""


def test_capitalize_none():
    # None вызывает AttributeError — это дефект, тест должен его ловить
    with pytest.raises(AttributeError):
        utils.capitalize(None)


# -------- trim --------

def test_trim_spaces():
    assert utils.trim("   skypro") == "skypro"


def test_trim_no_spaces():
    assert utils.trim("skypro") == "skypro"


def test_trim_only_spaces():
    # trim("   ") → "" — корректно
    assert utils.trim("   ") == ""


def test_trim_empty_string():
    assert utils.trim("") == ""


def test_trim_none():
    # None вызывает AttributeError — это дефект
    with pytest.raises(AttributeError):
        utils.trim(None)


# -------- contains --------

def test_contains_true():
    assert utils.contains("SkyPro", "S") is True


def test_contains_false():
    assert utils.contains("SkyPro", "U") is False


def test_contains_empty_string():
    assert utils.contains("", "a") is False


def test_contains_empty_symbol():
    # "" всегда находится в строке → True
    assert utils.contains("abc", "") is True


def test_contains_none_string():
    with pytest.raises(AttributeError):
        utils.contains(None, "a")


def test_contains_none_symbol():
    with pytest.raises(AttributeError):
        utils.contains("SkyPro", None)


# -------- delete_symbol --------

def test_delete_symbol_single():
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"


def test_delete_symbol_substring():
    assert utils.delete_symbol("SkyPro", "Pro") == "Sky"


def test_delete_symbol_not_found():
    assert utils.delete_symbol("SkyPro", "X") == "SkyPro"


def test_delete_symbol_multiple():
    assert utils.delete_symbol("aaaaa", "a") == ""


def test_delete_symbol_empty_symbol():
    # replace("", "") возвращает исходную строку
    assert utils.delete_symbol("abc", "") == "abc"


def test_delete_symbol_none_string():
    with pytest.raises(AttributeError):
        utils.delete_symbol(None, "a")


def test_delete_symbol_none_symbol():
    with pytest.raises(AttributeError):
        utils.delete_symbol("SkyPro", None)
