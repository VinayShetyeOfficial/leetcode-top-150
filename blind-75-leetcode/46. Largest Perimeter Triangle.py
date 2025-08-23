# ============================================
# Largest Perimeter Triangle - LeetCode
# ============================================

# ---------------------------
# Solution 1: Sort + Check Triplets
# ---------------------------
class Solution1(object):
    def largestPerimeter(self, nums): 
        nums.sort(reverse=True)  # Sort in descending order
        
        # Check triplets from largest to smallest
        for i in range(len(nums) - 2):
            if nums[i] < nums[i + 1] + nums[i + 2]:
                return nums[i] + nums[i + 1] + nums[i + 2]
        
        return 0

"""
Time Complexity (TC): O(n log n)
   - Sorting the array dominates the complexity
Space Complexity (SC): O(1)
   - Sorting in-place, no extra space except loop variables
"""

# ---------------------------
# Solution 2: Optimized using unpacking
# ---------------------------
class Solution2(object):
    def largestPerimeter(self, nums):
        if len(nums) < 3: 
            return 0
        
        nums.sort(reverse=True)
        a, b = nums[:2]  # largest two sides
        
        for c in nums[2:]:
            if b + c > a:
                return a + b + c
            a, b = b, c  # shift the window
        
        return 0

"""
Time Complexity (TC): O(n log n)
   - Sorting dominates, then linear scan of array
Space Complexity (SC): O(1)
   - Constant extra space, no new array created
"""

# ============================================
# Driver Code
# ============================================
if __name__ == '__main__':
    nums = [1, 2, 1, 10]
    
    # Test Solution1
    obj1 = Solution1()
    print("Solution1:", obj1.largestPerimeter(nums.copy()))
    
    # Test Solution2
    obj2 = Solution2()
    print("Solution2:", obj2.largestPerimeter(nums.copy()))
