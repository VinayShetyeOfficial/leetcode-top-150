# Link: https://takeuforward.org/plus/dsa/problems/remove-duplicates-from-sorted-array

# Remove duplicates from sorted array

def removeDuplicates(nums: list[int]) -> list[int]:
    n = len(nums)
    if n == 0:
        return nums
    
    writePtr = 1  # Pointer for placing unique elements
    for readPtr in range(1, n):
        if nums[readPtr] != nums[readPtr - 1]:
            nums[writePtr] = nums[readPtr]
            writePtr += 1
    
    # Optional: fill remaining positions with placeholder '_'
    for i in range(writePtr, n):
        nums[i] = '_'
    
    print(f'Count of unique elements: {writePtr}')
    return nums
    
if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4]
    ans = removeDuplicates(nums)
    print("Resulting Array:", ans)
# Resulting Array: [1, 2, 3, 4, '_', '_', '_', '_', '_', '_', '_']

'''
Time Complexity (TC):
-------------------
- O(N), where N is the length of the array. We traverse the array once.

Space Complexity (SC):
--------------------
- O(1), as we are modifying the array in-place without using extra space.
'''
