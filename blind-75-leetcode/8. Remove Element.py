# Link: https://leetcode.com/problems/remove-element/description/

# Remove Element
class Solution(object):
    def removeElement(self, nums, val):
        # Initialize a pointer to keep track of the position of elements not equal to val
        insert_pos = 0
    
        # Iterate through the array
        for i in range(len(nums)):
            if nums[i] != val:
                # Place the element at the insert position
                nums[insert_pos] = nums[i]
                # Move the insert position forward
                insert_pos += 1
    
        # The length of the array after removing val is insert_pos
        return insert_pos

# Driver code        
if __name__ == "__main__":
    obj = Solution()

    nums1 = [3, 2, 2, 3]
    val1 = 3
    k1 = obj.removeElement(nums1, val1)
    print(f'Input Array: {nums1}')
    print("Number of elements after removing {}: {}".format(val1, k1))
    print("Updated array:", nums1[:k1])
    
    print('')
    
    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    val2 = 2
    k2 = obj.removeElement(nums2, val2)
    print(f'Input Array: {nums2}')
    print("Number of elements after removing {}: {}".format(val2, k2))
    print("Updated array:", nums2[:k2])
   