"""
Time O(N) Space O(N)
Given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def add_two_numbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        pointer = result
        carry = 0
        while l1 or l2:
            current_sum = carry
            if l1:
                current_sum += l1.val
                l1 = l1.next
            if l2:
                current_sum += l2.val
                l2 = l2.next
            carry = int(current_sum/10)
            remainder = current_sum % 10
            pointer.next = ListNode(remainder)
            pointer = pointer.next
        if carry == 1:
            pointer.next = ListNode(carry)
        return result.next


