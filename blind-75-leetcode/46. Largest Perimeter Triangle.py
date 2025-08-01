# Link: https://leetcode.com/problems/largest-perimeter-triangle/description/

# Largest Perimeter Triangle
# ⭐ Solution 1
class Solution(object):
    def largestPerimeter(self, nums): 
        nums.sort(reverse=True)
        
        for i in range(len(nums) - 2):
            if nums[i] < nums[i + 1] + nums[i + 2]:
                return nums[i] + nums[i + 1] + nums[i + 2]
        
        return 0
    
# Driver code
if __name__ == '__main__':
    obj = Solution()
    nums = [1,2,1,10]
    print(obj.largestPerimeter(nums))
    

# =======================================================

# Another Solution   
class Solution(object):
    def largestPerimeter(self, nums):
        if len(nums) < 3: return 0
        
        nums.sort(reverse=True)
        a, b = nums[:2]
    
        for c in nums[2:]:
            if b + c > a:
                return a + b + c
            a, b = b, c
        return 0
    
# Driver code
if __name__ == '__main__':
    obj = Solution()
    nums = [1,2,1,10]
    print(obj.largestPerimeter(nums))
    