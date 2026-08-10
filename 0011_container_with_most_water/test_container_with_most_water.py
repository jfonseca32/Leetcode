import pytest
from container_with_most_water import Solution


@pytest.mark.parametrize(
    "height, expected",
    [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
    ],
)
class TestContainerWithMostWater:
    def test_max_area(self, height: list[int], expected: int):
        result: int = Solution().maxArea(height)

        assert result == expected
