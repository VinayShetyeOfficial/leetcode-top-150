# Remove duplicates from sorted array

def removeDuplicates(nums: list[int]) -> list[int]:
    n = len(nums)
    writePtr = 1
    for readPtr in range(1, n):
        if nums[readPtr] != nums[readPtr - 1]:
            nums[writePtr] = nums[readPtr]
            writePtr += 1
    
    for i in range(writePtr, len(nums)):
        nums[i] = '_'
    
    print(f'Count of unique elements: {writePtr}')
    
    return nums
    
if __name__ == "__main__":
    nums = [1,1,1,2,2,3,3,3,3,4,4]
    ans = removeDuplicates(nums)
    print("Resulting Array:", ans)