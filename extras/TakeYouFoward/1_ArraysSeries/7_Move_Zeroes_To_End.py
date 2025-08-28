# Link: https://takeuforward.org/plus/dsa/problems/move-zeros-to-end

# Move all Zeros to the end of the array

def moveZerosToEnd(nums: list[int]) -> list[int]:
    writePtr = 0  # Pointer to place non-zero elements
    for readPtr in range(len(nums)):
        if nums[readPtr] != 0:
            nums[writePtr] = nums[readPtr]
            writePtr += 1
    
    # Fill the remaining positions with zeros
    for i in range(writePtr, len(nums)):
        nums[i] = 0
        
    return nums
    
if __name__ == "__main__":
    nums = [1, 0, 2, 3, 0, 4, 0, 1]
    ans = moveZerosToEnd(nums)
    print("Resulting Array:", ans)
# Resulting Array: [1, 2, 3, 4, 1, 0, 0, 0]


'''
Time Complexity (TC):
-------------------
- O(N), where N is the length of the array. We traverse the array twice (once for moving non-zeros and once for filling zeros).

Space Complexity (SC):
--------------------
- O(1), as we are doing the operations in-place without using extra space.
'''
