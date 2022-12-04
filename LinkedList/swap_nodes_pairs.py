"""
Time O(N) Space O(1) - Iterate Solution
Time O(N) Space O(N) - Recursive Solution

Given a linked list, swap every two adjacent nodes and return its head.
You must solve the problem without modifying the values in the list's nodes (only nodes themselves may be changed)
[1, 2, 3, 4]
temp = head.next
head.next = swap(temp.next)
temp.next = head
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class RecursiveSolution:
    def swap_pairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            second = head.next  # 2
            head.next = self.swap_pairs(second.next)  # 1->(4,3)
            second.next = head  # 2->1
            return second  # return the new head
        return head  # return final update head


class IterativeSolution:
    def swap_pairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        result = prev = ListNode()
        prev.next = head  # create the dummy
        while head and head.next:
            second = head.next  # 2
            head.next = second.next  # 1->3
            second.next = head  # 2->1
            # Updates for head and prev
            prev.next = second
            prev = head
            head = head.next
        return result.next
