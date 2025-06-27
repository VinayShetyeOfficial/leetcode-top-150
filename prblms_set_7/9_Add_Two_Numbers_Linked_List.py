# 2. Add Two Numbers (Medium) - Done
# https://leetcode.com/problems/add-two-numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()      # Dummy node to build the result list
        cur = dummy             # Pointer to the current node in result
        carry = 0               # To handle carry over values during addition

        # Traverse both lists till all digits and carry are processed
        while l1 or l2 or carry:
            # Take values from nodes if they exist, else use 0
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            # Total sum of digits and carry
            total = v1 + v2 + carry
            carry = total // 10        # New carry
            val = total % 10           # Digit to store in node
            
            # Create new node with computed digit
            cur.next = ListNode(val)
            cur = cur.next

            # Move to next nodes if available
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next  # Return the result list starting from next of dummy


"""
✅ Time Complexity: O(max(n, m))
We iterate through both linked lists once.

n and m are lengths of l1 and l2.

✅ Space Complexity: O(max(n, m))
We create a new linked list to store the result.

In the worst case, an extra node might be added for a final carry.
"""
