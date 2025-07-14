# Find_the_number_that_appears_once / Single Number

def singleNumber(nums: list[int]) -> int:
    n = len(nums)
    res = 0
    
    for num in nums:
        res ^= num
        
    return res

if __name__ == "__main__":
    nums = [1, 2, 2, 4, 3, 1, 4]
    ans = singleNumber(nums)
    print("Single Number:", ans)

# Single Number: 3