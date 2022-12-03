"""
Time O(N) Space(1)
Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def remove_nth_from_end(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        result = ListNode()
        result.next = head
        first = result
        second = result
        for i in range(1, n+2):
            first = first.next
        while first:
            first = first.next
            second = second.next
        second.next = second.next.next
        return result.next
