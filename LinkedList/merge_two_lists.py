"""
Time O(N) Space(1)
You are given two sorted linked lists list1 and list2.Merge the two lists in a one sorted list.
The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge_two_lists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode(0)
        result = node
        while list1 and list2:
            if list1.val <= list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.val
            node = node.next
        remaining_list = list1 if list1 else list2
        while remaining_list:
            node.next = remaining_list
            remaining_list = remaining_list.next
            node = node.next
        return result.next
