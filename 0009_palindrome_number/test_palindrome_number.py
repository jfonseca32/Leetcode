import pytest
from palindrome_number import Solution


@pytest.mark.parametrize(
    "x, expected",
    [
        (121, True),
        (-121, False),
        (10, False),
        (10001, True),
        (119898911, True),
        (1111111, True),
        (1235982, False),
    ],
)
class TestIsPalindrome:
    def test_is_palindrome(self, x, expected):
        result = Solution().isPalindrome(x)

        assert expected == result
