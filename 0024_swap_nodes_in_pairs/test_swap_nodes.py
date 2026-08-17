import pytest
from swap_nodes import ListNode, Solution


@pytest.mark.parametrize(
    ("head", "expected"),
    [
        ([1, 2, 3, 4], [2, 1, 4, 3]),
        ([], []),
        ([1], [1]),
        ([1, 2, 3], [2, 1, 3]),
    ],
)
class TestSwapNodes:
    def test_swap_nodes(self, head: ListNode | None, expected: ListNode | None):
        result_node: ListNode | None = Solution().swapPairs(ListNode.from_list(head))

        assert (result_node.to_list() if result_node else []) == expected
