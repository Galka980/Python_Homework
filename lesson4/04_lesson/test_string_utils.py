# test_string_utils.py
import pytest
from string_utils import StringUtils


class TestStringUtils:

    @pytest.fixture
    def utils(self):
        return StringUtils()

    # Тесты для capitalize
    @pytest.mark.parametrize("input_str, expected", [
        ("skypro", "Skypro"),
        ("SkyPro", "SkyPro"),
        ("", ""),
        ("hello world", "Hello world"),
        ("123abc", "123abc"),
        (" тест", " тест"),  # пробел в начале
    ])
    def test_capitalize_positive(self, utils, input_str, expected):
        assert utils.capitalize(input_str) == expected

    # Тесты для trim
    @pytest.mark.parametrize("input_str, expected", [
        ("   skypro", "skypro"),
        ("  hello  ", "hello  "),  # удаляются только начальные пробелы
        ("", ""),
        ("test", "test"),
        ("\t\n test", "test"),  # удаляются и табуляции/переносы
    ])
    def test_trim_positive(self, utils, input_str, expected):
        assert utils.trim(input_str) == expected

    # Тесты для contains
    @pytest.mark.parametrize("string, symbol, expected", [
        ("SkyPro", "S", True),
        ("SkyPro", "U", False),
        ("", "a", False),
        ("hello", "ll", True),
        ("hello", "", True),  # пустая строка всегда содержится
        ("Test", "t", False),  # регистрозависимо
    ])
    def test_contains(self, utils, string, symbol, expected):
        assert utils.contains(string, symbol) == expected

    # Тесты для delete_symbol
    @pytest.mark.parametrize("string, symbol, expected", [
        ("SkyPro", "k", "SyPro"),
        ("SkyPro", "Pro", "Sky"),
        ("aaaa", "a", ""),
        ("test", "x", "test"),
        ("banana", "na", "ba"),
        ("", "a", ""),
    ])
    def test_delete_symbol(self, utils, string, symbol, expected):
        assert utils.delete_symbol(string, symbol) == expected

    # Тесты для starts_with
    @pytest.mark.parametrize("string, symbol, expected", [
        ("SkyPro", "S", True),
        ("SkyPro", "P", False),
        ("", "", True),
        ("hello", "he", True),
        ("hello", "lo", False),
    ])
    def test_starts_with(self, utils, string, symbol, expected):
        assert utils.starts_with(string, symbol) == expected

    # Тесты для end_with
    @pytest.mark.parametrize("string, symbol, expected", [
        ("SkyPro", "o", True),
        ("SkyPro", "y", False),
        ("", "", True),
        ("hello", "lo", True),
        ("hello", "he", False),
    ])
    def test_end_with(self, utils, string, symbol, expected):
        assert utils.end_with(string, symbol) == expected

    # Тесты для is_empty
    @pytest.mark.parametrize("string, expected", [
        ("", True),
        (" ", True),
        ("  ", True),
        ("SkyPro", False),
        ("\t\n", True),  # табуляции и переносы
        (" a ", False),  # пробелы с символом
    ])
    def test_is_empty(self, utils, string, expected):
        assert utils.is_empty(string) == expected

    # Тесты для list_to_string
    @pytest.mark.parametrize("lst, joiner, expected", [
        ([1, 2, 3, 4], ", ", "1, 2, 3, 4"),
        (["Sky", "Pro"], ", ", "Sky, Pro"),
        (["Sky", "Pro"], "-", "Sky-Pro"),
        ([], ", ", ""),
        (["single"], ", ", "single"),
        ([1, None, "test"], ", ", "1, None, test"),
    ])
    def test_list_to_string(self, utils, lst, joiner, expected):
        if joiner == ", ":
            assert utils.list_to_string(lst) == expected
        else:
            assert utils.list_to_string(lst, joiner) == expected

    # Негативные тесты (опционально)
    def test_capitalize_non_string(self, utils):
        # Тест на неправильный тип данных
        with pytest.raises(AttributeError):
            utils.capitalize(123)

    def test_contains_non_string_input(self, utils):
        # Проверяем поведение с нестроковыми символами
        assert utils.contains("test123", 1) == False  # число как символ

        # Инициализация класса
        utils = StringUtils()

        # starts_with
        print(utils.starts_with("Hello", "H"))  # True
        print(utils.starts_with("Hello", "h"))  # False

        # ends_with
        print(utils.ends_with("World", "d"))  # True
        print(utils.ends_with("World", "D"))  # False

        # is_empty
        print(utils.is_empty(""))  # True
        print(utils.is_empty("   "))  # True
        print(utils.is_empty(None))  # True
        print(utils.is_empty("Hello"))  # False

        # list_to_string
        print(utils.list_to_string([1, 2, 3]))  # "1, 2, 3"
        print(utils.list_to_string(["a", "b", "c"], " - "))  # "a - b - c"
        print(utils.list_to_string([True, False, None]))  # "True, False, None"