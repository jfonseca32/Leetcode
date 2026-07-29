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
    def addTwoNumbers(
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:
        head = ListNode()  # instantiate output with dummy head
        current = head  # pointer starts at head
        remainder = 0  # first remainder always 0

        while l1 or l2 or remainder:
            val1 = l1.val if l1 else 0  # get value if exists
            val2 = l2.val if l2 else 0

            total = val1 + val2 + remainder
            remainder = total // 10  # remainder (division) to carry

            current.next = ListNode(total % 10)  # digit (modulo) to list
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next  # advance lists

        return head.next
