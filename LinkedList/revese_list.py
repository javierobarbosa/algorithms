"""
Time O(N) Space O(1)
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = None
        while head:
            next_node = head.next
            head.next = prev_node
            prev_node = head
            head = next_node
        return prev_node

