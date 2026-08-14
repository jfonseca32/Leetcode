from __future__ import annotations


class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None):
        self.val: int = val
        self.next: ListNode | None = next

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
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        if not head:
            return None

        dummy = ListNode(0, head)
        tail: ListNode = dummy
        to_remove: ListNode = dummy

        # find the size of the linked list
        length = 0
        while tail.next:
            length += 1
            tail = tail.next

        traverse = length - n  # how many nodes we need to move from head
        while (
            traverse > 0 and to_remove.next
        ):  # to_remove.next at end will be node to remove
            traverse -= 1
            to_remove = to_remove.next

        # skip over the node to be removed
        to_remove.next = to_remove.next.next if to_remove.next else None

        return dummy.next
