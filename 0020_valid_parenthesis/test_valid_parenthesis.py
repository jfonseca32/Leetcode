import pytest
from valid_parenthesis import Solution


@pytest.mark.parametrize(
    ("s", "expected"),
    [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([])", True),
        ("([)]", False),
        ("()({})(([]))", True),
    ],
)
class TestValidParenthesis:
    def test_valid_parenthesis(self, s: str, expected: bool):
        result: bool = Solution().isValid(s)

        assert result == expected
