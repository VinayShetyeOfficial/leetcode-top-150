# 61. Rotate List (Medium) - Done
# https://leetcode.com/problems/rotate-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # Step 1: Find the length of the list and get the tail node
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # Step 2: Normalize k (if k >= length)
        k = k % length
        if k == 0:
            return head

        # Step 3: Find the new tail (at position length - k - 1)
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next

        # Step 4: Cut and rotate
        new_head = new_tail.next
        new_tail.next = None
        tail.next = head  # Link the old tail to the old head

        return new_head

"""
✅ Time Complexity
O(N) — You traverse the list twice: once to get the length and once to reach the breaking point.

N = number of nodes in the list.

✅ Space Complexity
O(1) — No extra space is used. Everything is done in-place.

"""