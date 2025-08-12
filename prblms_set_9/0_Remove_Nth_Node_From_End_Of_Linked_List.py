# 19. Remove Nth Node From End of List (Medium) - Done
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Preferred Solution:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left, right = dummy, head

        while n > 0 and right:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next
        return dummy.next



"""
✅ Time Complexity: O(N)

You traverse the list twice at most:

Once to move right pointer n steps ahead.

Once to move both left and right until right hits the end.

🔹 So overall, it’s linear in terms of number of nodes N.
"""


# Alternate Solution
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Step 1: Create a dummy node to handle edge cases like removing the first node
        dummy = ListNode(0)
        dummy.next = head
        
        # Step 2: Find the total length of the list
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        
        # Step 3: Find the node before the one we need to remove
        length -= n
        current = dummy
        for _ in range(length):
            current = current.next
        
        # Step 4: Remove the nth node
        current.next = current.next.next
        
        # Step 5: Return the new head
        return dummy.next


"""
| Complexity Type | Value  | Why?                                            |
| --------------- | ------ | ----------------------------------------------- |
| Time (TC)       | `O(L)` | One pass to count nodes, another to remove node |
| Space (SC)      | `O(1)` | Only a few pointers used, no extra space        |
"""