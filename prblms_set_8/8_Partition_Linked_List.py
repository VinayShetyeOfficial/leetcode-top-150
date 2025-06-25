# 86. Partition List (Medium) - Done
# https://leetcode.com/problems/partition-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Dummy nodes to build two separate lists
        left = ListNode(0)   # nodes < x
        right = ListNode(0)  # nodes >= x

        ltail, rtail = left, right  # tails for building both lists

        while head:
            if head.val < x:
                ltail.next = head
                ltail = ltail.next
            else:
                rtail.next = head
                rtail = rtail.next
            head = head.next

        # End the right list
        rtail.next = None
        # Connect left list with right list
        ltail.next = right.next

        return left.next
    
    
"""
| Metric               | Value                                                |
| -------------------- | ---------------------------------------------------- |
| **Time Complexity**  | `O(N)` — You go through the list once.               |
| **Space Complexity** | `O(1)` — No extra memory, just rearranging pointers. |

"""
