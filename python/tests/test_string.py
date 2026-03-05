"""Tests for string_utils module."""
from python.string_utils import reverse, is_palindrome, word_count, capitalize_words


class TestReverse:
    def test_basic(self):
        assert reverse("hello") == "olleh"

    def test_empty(self):
        assert reverse("") == ""

    def test_single_char(self):
        assert reverse("a") == "a"


class TestIsPalindrome:
    def test_palindrome(self):
        assert is_palindrome("racecar") is True

    def test_not_palindrome(self):
        assert is_palindrome("hello") is False

    def test_case_insensitive(self):
        assert is_palindrome("Racecar") is True

    def test_with_spaces(self):
        assert is_palindrome("race car") is True


class TestWordCount:
    def test_basic(self):
        assert word_count("hello world") == 2

    def test_empty(self):
        assert word_count("") == 0

    def test_whitespace_only(self):
        assert word_count("   ") == 0

    def test_single_word(self):
        assert word_count("hello") == 1


class TestCapitalizeWords:
    def test_basic(self):
        assert capitalize_words("hello world") == "Hello World"

    def test_already_capitalized(self):
        assert capitalize_words("Hello World") == "Hello World"

    def test_single_word(self):
        assert capitalize_words("hello") == "Hello"
