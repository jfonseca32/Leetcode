import pytest
from generate_parenthesis import Solution


@pytest.mark.parametrize(
    ("n", "expected"),
    [
        (3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),
        (1, ["()"]),
    ],
)
class TestGenerateParenthesis:
    def test_generate_parenthesis(self, n: int, expected: list[str]):
        result: list[str] = Solution().generateParenthesis(n)

        assert result == expected
