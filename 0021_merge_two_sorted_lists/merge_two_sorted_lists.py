from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    @classmethod
    def from_list(cls, values: list[int]) -> Optional["ListNode"]:
        head: ListNode | None = None
        for value in reversed(values):
            head = cls(value, head)
        return head

    def to_list(self) -> list[int]:
        values = []
        current: ListNode | None = self
        while current:
            values.append(current.val)
            current = current.next
        return values


class Solution:
    def mergeTwoLists(
        self, list1: ListNode | None, list2: ListNode | None
    ) -> ListNode | None:
        head = ListNode()
        current_node = head  # to build the list

        while list1 and list2:
            if list1.val <= list2.val:
                current_node.next = list1  # append to result
                list1 = list1.next  # walk input
            else:
                current_node.next = list2
                list2 = list2.next

            current_node = current_node.next  # walk output

        # append the rest of the one non-empty list
        current_node.next = list1 if list1 else list2
        return head.next  # next as first val is 0
