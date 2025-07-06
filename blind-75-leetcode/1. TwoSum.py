# Link: https://leetcode.com/problems/two-sum/description/

# Two Sum 
class Solution(object):
    def sum(self, nums, target):
        num_indices = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in num_indices:
                return (num_indices[complement], i)
        
            num_indices[num] = i
        
        return None

if __name__ == "__main__":
    obj = Solution()
    nums = [1,4,7,2,0,9]
    target = 9
    print(obj.sum(nums, target))