# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

# Remove Duplicates from Sorted Array
class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        unique_index = 0  # points to last unique element
        
        for i in range(1, len(nums)):
            if nums[i] != nums[unique_index]:
                unique_index += 1
                nums[unique_index] = nums[i]
        
        return unique_index + 1


# Driver code   
if __name__ == "__main__":
    obj = Solution()
    nums = [0,0,1,1,1,2,2,3,3,4]
    k = obj.removeDuplicates(nums)
    print("Number of unique elements:", k)         # Expected: 5
    print("Updated array:", nums[:k])              # Expected: [0,1,2,3,4]


"""
===========================================
Time Complexity (TC): O(n)
- We traverse the array once (n = length of nums).

Space Complexity (SC): O(1)
- In-place modification, no extra data structure used.
===========================================
"""
