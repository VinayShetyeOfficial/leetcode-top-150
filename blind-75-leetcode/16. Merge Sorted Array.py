# Link: https://leetcode.com/problems/merge-sorted-array/description/

# Merge Sorted Array
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Initialize the pointers
        # Satrt filling from back of nums1
        i = m - 1 # Last valid element in nums1
        j = n - 1 # Last element in nums2
        k = m + n - 1 # Last index in nums1 

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # Add if any leftover elements in nums2
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

# Time Complexity: O(m + n)
# Space Complexity: O(1)

# ============================================

# Alternate Solution   

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1[m:] = nums2
        
        size = m + n
        for i in range(size):
            for j in range(0, size - i - 1):
                if nums1[j] > nums1[j + 1]:
                    nums1[j], nums1[j + 1] = nums1[j + 1], nums1[j]
                    
        return nums1
    
# Driver code
if __name__ == '__main__':
    obj = Solution()
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    print(obj.merge(nums1, m, nums2, n))
    
