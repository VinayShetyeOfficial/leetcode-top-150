# Link: https://leetcode.com/problems/intersection-of-two-arrays-ii/description/

#  Intersection of Two Arrays II
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = Counter(nums1)
        result = []
        for num in nums2:
            if count1[num] > 0:
                result.append(num)
                count1[num] -= 1

        return result        

# ============================================

# Alternate Solution
from collections import Counter

class Solution(object):
    def intersect(self, nums1, nums2):
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        
        intersection = []
        for num in count1:
            if num in count2:
                intersection.extend([num] * min(count1[num], count2[num]))
        
        return intersection
    
# Driver code
if __name__ == '__main__':
    obj = Solution()
    nums1 = [1,2]
    nums2 = [1,1]
    print(obj.intersect(nums1, nums2))

# ============================================

# Another Solution
class Solution(object):
    def intersect(self, nums1, nums2):
        res = []
        for i in nums1:
            if i in nums2 and res.count(i) < nums2.count(i):
                res.append(i)
        return res
        
# Driver code
if __name__ == '__main__':
    obj = Solution()
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    print(obj.intersect(nums1, nums2))
