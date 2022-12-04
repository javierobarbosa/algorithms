"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.
"""
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge_k_lists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        i = 0
        last = len(lists) - 1
        j = last
        while last != 0:
            i = 0
            j = last
            while j > i:
                lists[i] = self.merge_two_lists(lists[i], lists[j])
                i += 1
                j -= 1
                last = j
        return lists[0]

    def merge_two_lists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = node = ListNode()
        while l1 and l2:
            if l1.val <= l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next
        while l1:
            node.next = l1
            l1 = l1.next
            node = node.next
        while l2:
            node.next = l2
            l2 = l2.next
            node = node.next
        return result.next
