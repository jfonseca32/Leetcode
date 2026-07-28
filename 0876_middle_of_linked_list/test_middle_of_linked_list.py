import pytest
from middle_of_linked_list import ListNode, Solution


@pytest.mark.parametrize(
    ("head", "expected"),
    [
        ([1, 2, 3, 4, 5], [3, 4, 5]),
        ([1, 2, 3, 4, 5, 6], [4, 5, 6]),
        ([1], [1]),
        ([1, 2], [2]),
    ],
)
class TestMiddleOfLinkedList:
    def test_middle_node(self, head, expected):
        head_node = ListNode.from_list(head)
        result_node = Solution().middleNode(head_node)

        assert result_node is not None
        assert result_node.to_list() == expected
