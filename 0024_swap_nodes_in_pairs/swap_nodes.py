from __future__ import annotations


class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None):
        self.val = val
        self.next = next

    @classmethod
    def from_list(cls, values: list[int]) -> ListNode | None:
        head: ListNode | None = None
        for value in reversed(values):
            head = cls(value, head)
        return head

    def to_list(self) -> list[int]:
        values: list[int] = []
        current: ListNode | None = self
        while current:
            values.append(current.val)
            current = current.next
        return values


class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return None

        dummy = ListNode(0, head)
        tail = dummy

        while tail.next and tail.next.next:
            first = tail.next  # get references
            second = tail.next.next
            first.next = second.next  # first node needs to point to third

            tail.next = second
            tail.next.next = first

            tail = tail.next.next  # advance tail

        return dummy.next
