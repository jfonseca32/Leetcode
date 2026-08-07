import pytest
from merge_two_sorted_lists import ListNode, Solution


@pytest.mark.parametrize(
    ("list1", "list2", "expected"),
    [
        ([1, 2, 3, 4, 5], [3, 4, 5], [1, 2, 3, 3, 4, 4, 5, 5]),
        ([1, 2, 3, 4, 5, 6], [4, 5, 6], [1, 2, 3, 4, 4, 5, 5, 6, 6]),
        ([1], [1], [1, 1]),
        ([1, 2], [2], [1, 2, 2]),
        ([], [], []),
    ],
)
class TestMergeTwoSortedLists:
    def test_merge_two_sorted_lists(self, list1, list2, expected):
        node1 = ListNode.from_list(list1)
        node2 = ListNode.from_list(list2)
        result_node = Solution().mergeTwoLists(node1, node2)

        assert (result_node.to_list() if result_node else []) == expected
