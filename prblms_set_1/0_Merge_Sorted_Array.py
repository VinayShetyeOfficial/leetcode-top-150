# 88. Merge Sorted Array (Easy) - Done
# https://leetcode.com/problems/merge-sorted-array

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Initialize pointers
        # Start filling from the back of nums1
        i = m - 1  # Last valid element in nums1
        j = n - 1  # Last element in nums2
        k = m + n - 1  # Last index in nums1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # If there are any leftover elements in nums2
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1


"""
⏱️ Time & Space Complexity:
---------------------------
✅ Time Complexity: O(m + n)
👉 Why?
You have two pointers: one iterating through nums1 (up to m elements) and one through nums2 (up to n elements).

In the worst case, you compare and/or copy each element of both arrays exactly once.

There are two loops:

The first while loop runs while i >= 0 and j >= 0, which can run up to min(m, n) times, but combined with the second loop:

The second while loop (if j >= 0) ensures that all elements of nums2 are placed into nums1.

➡️ So overall, you are doing at most m + n operations, hence:

✅ Time Complexity = O(m + n)
✅ Space Complexity = O(1)
Everything is done in-place.

No extra arrays or data structures are used.

Only a few integer pointers (i, j, k) — constant space.
"""