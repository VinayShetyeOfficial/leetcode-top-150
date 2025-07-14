# Move all Zeros to the end of the array

def moveZerosToEnd(nums: list[int]) -> int:
    writePtr = 0
    for readPtr in range(len(nums)):
        if nums[readPtr] != 0:
            nums[writePtr] = nums[readPtr]
            writePtr += 1
    
    for i in range(writePtr, len(nums)):
        nums[i] = 0
        
    return nums
    
if __name__ == "__main__":
    nums = [1 ,0 ,2 ,3 ,0 ,4 ,0 ,1]
    ans = moveZerosToEnd(nums)
    print("Resulting Array:", ans)
    
# Resulting Array: [1, 2, 3, 4, 1, 0, 0, 0]