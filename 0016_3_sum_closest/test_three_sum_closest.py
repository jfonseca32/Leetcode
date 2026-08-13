import pytest
from three_sum_closest import Solution


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([-1, 2, 1, -4], 1, 2),
        ([0, 0, 0], 1, 0),
        ([1, 1, 1, 0], 100, 3),
    ],
)
class TestThreeSumClosest:
    def test_three_sum_closest(self, nums: list[int], target: int, expected: int):
        result: int = Solution().threeSumClosest(nums, target)

        assert result == expected
