import pytest
from letter_combination_of_a_phone_number import Solution


@pytest.mark.parametrize(
    ("digits", "expected"),
    [
        ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
        ("2", ["a", "b", "c"]),
    ],
)
class TestLetterCombinations:
    def test_letter_combination(self, digits: str, expected: list[str]):
        result: list[str] = Solution().letterCombinations(digits)

        assert result == expected
