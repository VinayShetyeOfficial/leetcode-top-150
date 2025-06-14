# 21. Merge Two Sorted Lists (Easy) - Done
# https://leetcode.com/problems/merge-two-sorted-lists

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merges two sorted linked lists into one sorted linked list.
        Uses a dummy node to simplify pointer handling.
        """

        # Dummy node to act as the head of the merged list
        dummy = ListNode()
        tail = dummy  # Tail tracks the last node in the merged list

        # Traverse both lists until one is exhausted
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # Attach any remaining elements
        tail.next = list1 if list1 else list2

        return dummy.next


"""
✅ Time Complexity: O(n + m)
👉 n = length of list1, m = length of list2

✅ Space Complexity: O(1)
👉 Uses only pointers, no extra data structures
"""
