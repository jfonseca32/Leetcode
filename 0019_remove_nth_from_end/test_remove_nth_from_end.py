import pytest
from remove_nth_from_end import ListNode, Solution


@pytest.mark.parametrize(
    ("head_list", "n", "expected"),
    [
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
        ([1], 1, []),
        ([1, 2], 1, [1]),
    ],
)
class TestRemoveNthFromEnd:
    def test_remove_nth_from_end(
        self, head_list: list[int], n: int, expected: list[int]
    ):
        head_node: ListNode | None = ListNode.from_list(head_list)
        result_node: ListNode | None = Solution().removeNthFromEnd(head_node, n)

        result: list[int] | None = [] if result_node is None else result_node.to_list()
        assert result == expected
