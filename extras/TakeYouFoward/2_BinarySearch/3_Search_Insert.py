# Link: https://takeuforward.org/plus/dsa/problems/search-insert-position

# Search Insert

def searchInsert(nums: int, target: int) -> int:
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return left

if __name__ == "__main__":
    arr = [3, 5, 8, 9, 15, 19]
    target = 17
    indx = searchInsert(arr, target)
    print("The insert index is:", indx)
