# 148. Sort List (Medium)
# https://leetcode.com/problems/sort-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head  # Base case

        # Step 1: Split the list into two halves
        mid = self.getMid(head)
        right = mid.next
        mid.next = None  # Break the list into two parts
        left = head

        # Step 2: Sort each half
        left = self.sortList(left)
        right = self.sortList(right)

        # Step 3: Merge both sorted halves
        return self.mergeList(left, right)

    # Helper to find middle of list
    def getMid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    # Helper to merge two sorted lists
    def mergeList(self, list1, list2):
        dummy = tail = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # Attach remaining elements
        tail.next = list1 if list1 else list2

        return dummy.next


"""
📈 Time & Space Complexity:
Time: O(n log n) — standard for merge sort

Space: O(log n) — due to recursion stack (not extra memory for nodes)
"""