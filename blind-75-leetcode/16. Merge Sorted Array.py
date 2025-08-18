# Link: https://leetcode.com/problems/merge-sorted-array/

# ============================================
# Optimal Solution (In-place from the end)
# ============================================

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
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

        # Add leftover elements from nums2 (if any)
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

"""
Time Complexity (TC): O(m + n)
- We traverse both arrays once.
Space Complexity (SC): O(1)
- In-place merging, no extra space used.
"""

# ============================================
# Alternate Solution (Append + Bubble Sort)
# ============================================

class AltSolution(object):
    def merge(self, nums1, m, nums2, n):
        # Replace trailing 0s in nums1 with nums2
        nums1[m:] = nums2
        
        size = m + n
        # Bubble sort to arrange elements
        for i in range(size):
            for j in range(0, size - i - 1):
                if nums1[j] > nums1[j + 1]:
                    nums1[j], nums1[j + 1] = nums1[j + 1], nums1[j]
                    
        return nums1

"""
Time Complexity (TC): O((m+n)^2)
- Bubble Sort runs in quadratic time.
Space Complexity (SC): O(1)
- Sorting is done in-place.
"""

# ============================================
# Driver Code
# ============================================
if __name__ == '__main__':
    # Optimal solution
    obj1 = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    obj1.merge(nums1, m, nums2, n)
    print("Optimal Solution:", nums1)   # Output: [1, 2, 2, 3, 5, 6]

    # Alternate solution
    obj2 = AltSolution()
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    print("Alternate Solution:", obj2.merge(nums1, m, nums2, n))  # Output: [1, 2, 2, 3, 5, 6]
