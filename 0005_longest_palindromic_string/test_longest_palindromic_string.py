import pytest
from longest_palindromic_string import Solution


@pytest.mark.parametrize(
    "s, expected",
    [
        ("babad", "bab"),
        ("cbbd", "bb"),
        ("a", "a"),
        ("ac", "a"),
        ("racecar", "racecar"),
        ("abccba", "abccba"),
        ("abcde", "a"),
    ],
)
class TestLongestPalindromicString:
    def test_longest_palindrome(self, s, expected):
        result = Solution().longestPalindrome(s)

        assert result == expected
