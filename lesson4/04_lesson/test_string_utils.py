import pytest
from StringUtils import StringUtils


@pytest.fixture
def string_utils():
    return StringUtils()


def test_capitilize(string_utils):
    assert string_utils.capitilize("skypro") == "Skypro"
    assert string_utils.capitilize("hello") == "Hello"
    assert string_utils.capitilize("") == ""


def test_trim(string_utils):
    assert string_utils.trim("   skypro   ") == "skypro"
    assert string_utils.trim("skypro   ") == "skypro"
    assert string_utils.trim("   skypro") == "skypro"
    assert string_utils.trim("skypro") == "skypro"
    assert string_utils.trim("   ") == ""
    assert string_utils.trim("") == ""


def test_to_list(string_utils):
    assert string_utils.to_list("a,b,c,d") == ["a", "b", "c", "d"]
    assert string_utils.to_list("1:2:3", ":") == ["1", "2", "3"]
    assert string_utils.to_list("", ",") == []
    assert string_utils.to_list("single") == ["single"]


def test_contains(string_utils):
    assert string_utils.contains("SkyPro", "S")
    assert not string_utils.contains("SkyPro", "U")


def test_delete_symbol(string_utils):
    assert string_utils.delete_symbol("SkyPro", "k") == "SyPro"
    assert string_utils.delete_symbol("SkyPro", "Pro") == "Sky"
    assert string_utils.delete_symbol("SkyPro", "Z") == "SkyPro"


def test_starts_with(string_utils):
    assert string_utils.starts_with("SkyPro", "S")
    assert not string_utils.starts_with("SkyPro", "P")


def test_end_with(string_utils):
    assert string_utils.end_with("SkyPro", "o")
    assert not string_utils.end_with("SkyPro", "y")


def test_is_empty(string_utils):
    assert string_utils.is_empty("")
    assert string_utils.is_empty(" ")
    assert not string_utils.is_empty("SkyPro")


def test_list_to_string(string_utils):
    assert string_utils.list_to_string([1, 2, 3, 4]) == "1, 2, 3, 4"
    assert string_utils.list_to_string(["Sky", "Pro"]) == "Sky, Pro"
    assert string_utils.list_to_string([], "-") == ""
    assert string_utils.list_to_string(["A", "B", "C"], "|") == "A|B|C"
