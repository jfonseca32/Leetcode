import pytest
from add_two_numbers import ListNode, Solution


@pytest.mark.parametrize(
    ("l1", "l2", "expected"),
    [
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
        ([0], [0], [0]),
        ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
    ],
)
class TestAddTwoNumbers:
    def test_add_two_numbers(self, l1, l2, expected):
        l1_node = ListNode.from_list(l1)
        l2_node = ListNode.from_list(l2)
        result_node = Solution().addTwoNumbers(l1_node, l2_node)

        assert result_node is not None
        assert result_node.to_list() == expected
