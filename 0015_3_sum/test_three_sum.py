import pytest
from three_sum import Solution


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([-1, 0, 1, 2], [[-1, 0, 1]]),
        ([0, 0, 0, 0], [[0, 0, 0]]),
        ([0, 0, 0], [[0, 0, 0]]),
        ([-1, 0, 1, 0], [[1, -1, 0]]),
        ([1, 2, 0, 1, 0, 0, 0, 0], [[0, 0, 0]]),
    ],
)
class TestThreeSum:
    def test_three_sum(self, nums: list[int], expected: list[list[int]]):
        result = Solution().threeSum(nums)

        assert sorted([sorted(x) for x in result]) == sorted(
            [sorted(x) for x in expected]
        )
