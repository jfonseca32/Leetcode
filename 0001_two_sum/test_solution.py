import pytest
from solution import Solution


@pytest.mark.parametrize(
    ("nums", "target"),
    [
        ([2, 7, 11, 15], 9),
        ([3, 3], 6),
        ([-3, 4, 3, 90], 0),
        ([0, 4, 3, 0], 0),
    ],
)
def test_two_sum(nums, target):
    result = Solution().twoSum(nums, target)

    assert len(result) == 2
    first, second = result
    assert first != second
    assert nums[first] + nums[second] == target
