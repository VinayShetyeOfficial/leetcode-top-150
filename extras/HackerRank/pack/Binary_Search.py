# https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/lookup-with-binary-search

def binarySearch(nums, target):
    # Write your code here
    low, high = 0, len(nums) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1
