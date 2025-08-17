# Link: https://leetcode.com/problems/search-insert-position/

# Search Insert Position
class Solution(object):
    def searchInsert(self, nums, target):
        low, high = 0, len(nums) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
                
        return low


# Driver code                
if __name__ == "__main__":
    obj = Solution()
    
    nums1 = [1, 3, 5, 6]
    target1 = 5
    print("Index of target {}: {}".format(target1, obj.searchInsert(nums1, target1)))  # Output: 2
    
    nums2 = [1, 3, 5, 6]
    target2 = 2
    print("Index of target {}: {}".format(target2, obj.searchInsert(nums2, target2)))  # Output: 1
    
    nums3 = [1, 3, 5, 6]
    target3 = 7
    print("Index of target {}: {}".format(target3, obj.searchInsert(nums3, target3)))  # Output: 4


"""
===========================================
Time Complexity (TC): O(log n)
- Binary search splits the array in half each iteration.

Space Complexity (SC): O(1)
- Only constant extra variables used (low, high, mid).
===========================================
"""
