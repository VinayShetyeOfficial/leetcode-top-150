# Link: https://leetcode.com/problems/intersection-of-two-arrays-ii/description/

# ============================================
# Solution 1: Using Counter for nums1
# ============================================
from collections import Counter
from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = Counter(nums1)
        result = []
        for num in nums2:
            if count1[num] > 0:
                result.append(num)
                count1[num] -= 1
        return result        

"""
Time Complexity: O(n + m) 
  - n = len(nums1), m = len(nums2)
  - Counting nums1: O(n)
  - Traversing nums2: O(m)
Space Complexity: O(n) for count1 dictionary
"""

# ============================================
# Solution 2: Using Counter for both arrays
# ============================================
class Solution(object):
    def intersect(self, nums1, nums2):
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        
        intersection = []
        for num in count1:
            if num in count2:
                intersection.extend([num] * min(count1[num], count2[num]))
        
        return intersection

"""
Time Complexity: O(n + m) 
  - Counting both arrays: O(n + m)
  - Constructing intersection: O(k), k = size of result
Space Complexity: O(n + m) for both counters
"""

# ============================================
# Solution 3: Brute-force approach
# ============================================
class Solution(object):
    def intersect(self, nums1, nums2):
        res = []
        for i in nums1:
            if i in nums2 and res.count(i) < nums2.count(i):
                res.append(i)
        return res

"""
Time Complexity: O(n * m) in worst case
  - For each element in nums1, counting in nums2 is O(m)
Space Complexity: O(k), k = size of result
"""

# ============================================
# Driver Code
# ============================================
if __name__ == '__main__':
    obj = Solution()
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    print("Intersection:", obj.intersect(nums1, nums2))
