# Link: https://leetcode.com/problems/squares-of-a-sorted-array/description/

# Squares of a Sorted Array

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n  # Final sorted squares
        left, right = 0, n - 1
        pos = n - 1  # Position to insert next largest square

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[pos] = nums[left] * nums[left]
                left += 1
            else:
                result[pos] = nums[right] * nums[right]
                right -= 1
            pos -= 1

        return result
    
# =======================================================

# Alternate Solution

class Solution(object):
    def sortedSquares(self, nums):
        
        nums = [x**2 for x in nums]
        # nums = list(map(lambda x:x**2, nums))    # Optional

        nums.sort()
        
        return nums
        # return sorted([x**2 for x in nums])      # Optional
    
# Driver code
if __name__ == '__main__':
    obj = Solution()
    nums = [-4,-1,0,3,10]
    print(obj.sortedSquares(nums))
    
