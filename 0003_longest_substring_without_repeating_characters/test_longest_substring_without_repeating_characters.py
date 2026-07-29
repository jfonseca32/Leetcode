import pytest
from longest_substring_without_repeating_characters import Solution


@pytest.mark.parametrize(
    "s, expected",
    [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        (" ", 1),
        ("au", 2),
        ("dvdf", 3),
    ],
)
class TestLengthOfLongestSubstring:
    def test_length_of_longest_substring(self, s, expected):
        solution = Solution()
        result = solution.lengthOfLongestSubstring(s)
        assert result == expected
