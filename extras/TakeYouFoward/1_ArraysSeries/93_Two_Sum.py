# Link: https://takeuforward.org/plus/dsa/problems/two-sum

# Two Sum

def twoSum(nums: list[int], target: int):
    seen = {}
    
    for index, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], index]
        seen[num] = index
        
    return -1
        
if __name__ == "__main__":
    nums = [1, 6, 2, 10, 3]
    target = 16
    ans = twoSum(nums, target)
    print(f'Indices: {ans}')
