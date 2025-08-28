# Link: https://takeuforward.org/plus/dsa/problems/maximum-consecutive-ones

# Count Maximum Consecutive 1's in an array

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

# Time Complexity (TC): O(n) → single pass through the array
# Space Complexity (SC): O(1) → only a few variables used


# =========================
# Count total 1-bits in array integers (Brian Kernighan’s Algorithm)
def findOnesCount(nums: list[int]) -> int:
    count = 0
    for num in nums:
        while num:
            num &= (num - 1)  # removes the lowest set bit
            count += 1
    return count

if __name__ == "__main__":
    nums = [5, 3]  # 5 -> 0101 (2 ones), 3 -> 0011 (2 ones)
    ans = findOnesCount(nums)
    print("The total count of 1's is", ans)

# Time Complexity (TC): O(total number of 1-bits in all numbers)
# Space Complexity (SC): O(1) → only a few variables used
