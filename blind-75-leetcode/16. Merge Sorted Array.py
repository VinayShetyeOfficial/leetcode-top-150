# Link: https://leetcode.com/problems/merge-sorted-array/description/

# Merge Sorted Array
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
    
