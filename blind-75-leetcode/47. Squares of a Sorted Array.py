# Link: https://leetcode.com/problems/squares-of-a-sorted-array/description/

# Squares of a Sorted Array
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
    
