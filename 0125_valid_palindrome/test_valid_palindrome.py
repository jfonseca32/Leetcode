import pytest
from valid_palindrome import Solution


@pytest.mark.parametrize(
    ("s", "expected"),
    [
        ("A man, a plan, a canal: Panama", True),
        ("racecar", True),
        ("", True),
        (" ", True),
        ("0P", False),
        ("race a car", False),
    ],
)
def test_is_palindrome(s, expected):
    result = Solution().isPalindrome(s)

    assert result == expected
