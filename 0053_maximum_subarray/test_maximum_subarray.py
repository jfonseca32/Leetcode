import pytest
from maximum_subarray import Solution


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1], 1),
        ([1, 2], 3),
        ([1, 2, 3], 6),
        ([1, 2, 3, -1], 6),
        ([1, 2, 3, -1, -2], 6),
        ([-2, 2, 7, -2, -100, 11, 6, -1, 2], 18),
        ([-2, 1], 1),
        ([-2, 1, -3], 1),
    ],
)
class TestMaximumSubarray:
    def test_max_subarray(self, nums, expected):
        solution = Solution()
        assert solution.maxSubArray(nums) == expected
