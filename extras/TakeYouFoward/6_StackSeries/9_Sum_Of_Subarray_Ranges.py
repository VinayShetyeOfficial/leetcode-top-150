# Sum of Subarray Ranges

def subarrayRanges(nums: list[int]) -> int:
    n = len(nums)
    total = 0
    
    for i in range(n):
        _min = _max = nums[i]
        for j in range(i, n):
            _min = min(_min, nums[j])
            _max = max(_max, nums[j])
            total += _max - _min
            
    return total
            

# ----------- Test Driver Code -----------
if __name__ == '__main__':
    test_cases = [
        [1, 2, 3],        # Output: 4
        [1, 3, 3],        # Output: 4
        [4, 1, 2],        # Output: 7
        [1],              # Output: 0
        [2, 2, 2],        # Output: 0
        [1, 5, 2, 4, 3],  # Try this
    ]

    for nums in test_cases:
        ans = subarrayRanges(nums)
        print(f'Nums: {nums} -> Subarray Ranges Sum: {ans}')
