# Binary Search

def binarySearch(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    
    while left <= right: 
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1

        
if __name__ == "__main__":
    nums =  [-1,0,3,5,9,12]
    target = 5
    ans = binarySearch(nums, target)
    print(f'Search Index: {ans}')