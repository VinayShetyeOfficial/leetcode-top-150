# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

# Remove Duplicates from Sorted Array
class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        unique_index = 0
        
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
    print("Number of unique elements: ", k)
    print("Updated array: ", nums[:k])
