import pytest
from four_sum import Solution


@pytest.mark.parametrize(
    ("nums", "target", "expected"),
    [
        ([1, 0, -1, 0, -2, 2], 0, [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]),
        ([2, 2, 2, 2, 2], 8, [[2, 2, 2, 2]]),
        ([-3, -1, 0, 2, 4, 5], 0, [[-3, -1, 0, 4]]),
        (
            [-3, -2, -1, 0, 0, 1, 2, 3],
            0,
            [
                [-3, -2, 2, 3],
                [-3, -1, 1, 3],
                [-3, 0, 0, 3],
                [-3, 0, 1, 2],
                [-2, -1, 0, 3],
                [-2, -1, 1, 2],
                [-2, 0, 0, 2],
                [-1, 0, 0, 1],
            ],
        ),
        ([-2, -1, -1, 1, 1, 2, 2], 0, [[-2, -1, 1, 2], [-1, -1, 1, 1]]),
    ],
)
class TestFourSum:
    def test_four_sum(self, nums: list[int], target: int, expected: list[list[int]]):
        result: list[list[int]] = Solution().fourSum(nums, target)

        assert result == expected
