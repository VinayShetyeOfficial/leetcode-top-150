# Find Missing Number

# 1. Using XOR Operation
def missingNumber(nums: list[int]) -> int:
    n = len(nums)
    res = 0
    
    # XOR all numbers from 0 to n
    for i in range(n + 1):
        res ^= i
    
    # XOR with all elements in the array
    for num in nums:
        res ^= num
        
    return res

if __name__ == "__main__":
    nums = [0, 1, 2, 4, 5, 6]
    ans = missingNumber(nums)
    print("Missing Number:", ans)



# 2. Using Arithmetic Operation
def missingNumber(nums: list[int]) -> int:
    n = len(nums)
    expected_total = (n * (n + 1)) // 2
    actual_total = sum(nums)
    return expected_total - actual_total

if __name__ == "__main__":
    nums = [0, 1, 2, 3, 5, 6]
    ans = missingNumber(nums)
    print("Missing Number:", ans)