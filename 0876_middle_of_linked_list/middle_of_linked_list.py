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
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next  # fast advance 2
            slow = slow.next  # slow advance 1

        return slow  # slow exactly (second) middle as fast reaches end
