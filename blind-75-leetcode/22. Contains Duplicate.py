# Link: https://leetcode.com/problems/contains-duplicate/description/

# Contains Duplicate
class Solution(object):
    def containsDuplicate(self, nums):

        hashset = set()     
        for i in nums:
            if i in hashset:
                    return True
            hashset.add(i) 
            
        return False
    
        # return not len(nums) == len(set(nums))     # Optional

if __name__ == "__main__":
    # Example usage:
    obj = Solution()
    nums = [1,1,1,3,3,4,3,2,4,2]
    print(obj.containsDuplicate(nums))