# Count Maximum Consecutive One's in the array

def findMaxConsecutiveOnes(nums: list[int]) -> int:
    count = 0
    max_consecutive_count = 0
    
    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1
        else:
            count = 0
            
        max_consecutive_count = max(max_consecutive_count, count)
        
    return max_consecutive_count

if __name__ == "__main__":
    nums = [1, 1, 0, 1, 1, 1]
    ans = findMaxConsecutiveOnes(nums)
    print("The maximum consecutive 1's are", ans)
    
# ===================================================================

# Finding count of 1 bits in integer num = 5 (0101) => 2
# Using Brian Kernighan’s Algorithm (Faster)
def findOnesCount(nums: list[int]) -> int:
    count = 0
    for num in nums:
        while num:
            num &= (num - 1)  # removes the lowest set bit
            count += 1
    return count

if __name__ == "__main__":
    nums = [1, 1]
    ans = findOnesCount(nums)
    print("The One's count is", ans)