import pytest
from string_to_integer import Solution


@pytest.mark.parametrize(
    "s, expected",
    [
        ("-042", -42),
        ("42", 42),
        ("1337c0d3", 1337),
        ("0-1", 0),
    ],
)
class TestMyAtoi:
    def test_my_atoi(self, s: str, expected: int):
        result = Solution().myAtoi(s)

        assert result == expected
