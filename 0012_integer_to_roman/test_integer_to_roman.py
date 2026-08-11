import pytest
from integer_to_roman import Solution


@pytest.mark.parametrize(
    "num, expected",
    [
        (3749, "MMMDCCXLIX"),
        (58, "LVIII"),
        (1994, "MCMXCIV"),
    ],
)
class TestIntegerToRoman:
    def test_integer_to_roman(self, num: int, expected: str):
        result = Solution().intToRoman(num)

        assert result == expected
