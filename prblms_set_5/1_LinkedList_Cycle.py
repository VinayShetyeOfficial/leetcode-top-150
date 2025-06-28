# 141. Linked List Cycle (Easy) - Done
# https://leetcode.com/problems/linked-list-cycle

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Detects if the linked list has a cycle using Floyd’s Cycle Detection algorithm.
        Uses two pointers (slow and fast) to detect a loop in O(1) space.
        """
        slow = fast = head

        while fast and fast.next:
            slow = slow.next         # move one step
            fast = fast.next.next    # move two steps

            if slow == fast:
                return True  # Cycle detected

        return False  # Reached the end, no cycle

"""
✅ Time Complexity: O(n)
👉 In the worst case, we may visit all nodes

✅ Space Complexity: O(1)
👉 Only two pointers used, no extra memory
"""