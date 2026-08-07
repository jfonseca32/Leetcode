import pytest
from longest_common_prefix import Solution


@pytest.mark.parametrize(
    "strs, expected",
    [
        (["flower", "flow", "flights"], "fl"),
        (["dog", "racecar", "car"], ""),
    ],
)
class TestLongestCommonPrefix:
    def test_longest_common_prefix(self, strs: list[str], expected) -> str:
        result = Solution().longestCommonPrefix(strs)

        assert expected == result
