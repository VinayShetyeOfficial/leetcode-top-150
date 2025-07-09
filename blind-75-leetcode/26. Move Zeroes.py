# Link: https://leetcode.com/problems/move-zeroes/

# Move Zeroes 
# ⭐ Solution1
--------------
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0

        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1

        return nums


# ----------------------

# Solution2
class Solution(object):
    def moveZeroes(self, nums):

        last_non_zero_found_at = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_non_zero_found_at] = nums[i]
                last_non_zero_found_at += 1
                
        for i in range(last_non_zero_found_at, len(nums)):
            nums[i] = 0

# Driver code
if __name__ == '__main__':
    obj = Solution()
    nums = [0,1,0,3,12]
    print(obj.moveZeroes(nums))

# ----------------------

# Solution3
class Solution(object):
    def moveZeroes(self, nums):
        
        nums[:] = [val for val in nums if val != 0] + [0 for i in range(nums.count(0))]
            
        return nums

# Driver code
if __name__ == '__main__':
    obj = Solution()
    nums = [0,1,0,3,12]
    print(obj.moveZeroes(nums))


# ----------------------

# Another Solution                  => Output Limit Exceede
class Solution(object):
    def moveZeroes(self, nums):
        n = len(nums)
        for i in range(n-1, -1, -1):
            if nums[i] == 0:
                nums.pop(i)
                print(nums)
                nums.insert(n-1, 0)
        return nums

# Driver code
if __name__ == '__main__':
    obj = Solution()
    nums = [0,1,0,3,12]
    print(obj.moveZeroes(nums))
