# Link: https://takeuforward.org/plus/dsa/problems/linear-search

# Search Insert Position (Binary Search approach)

def searchInsertPos(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return left  # insertion index if not found

if __name__ == "__main__":
    arr = [1, 2, 4, 5, 7, 8, 9, 10]
    target = 6
    print(f'Index: {searchInsertPos(arr, target)}')  # Output: 4


# ==============================================================

# Binary Search with Random Target
import random

def compute(nums: list[int]) -> None:
    nums.sort()
    left, right = 0, len(nums) - 1
    target = random.choice(nums)
    print(f'Nums: {nums}, target: {target}')
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            print(mid)
            break
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    else:
        print(-1)

if __name__ == '__main__':
    arr = [random.randint(1, 100) for _ in range(10)]
    compute(arr)


# ==============================================================

# Using inbuilt `bisect` method
import bisect

arr = [2, 4, 6, 8, 10, 12]
target = 8

index = bisect.bisect_left(arr, target)

if index < len(arr) and arr[index] == target:
    print(f"Element found at index {index}")
else:
    print("Element not found")


'''
Time Complexity (TC):
-------------------
1. searchInsertPos (binary search) : O(log N)
2. compute (binary search on sorted array) : 
   - Sorting → O(N log N)
   - Binary Search → O(log N)
   → Overall O(N log N)
3. bisect.bisect_left : O(log N)

Space Complexity (SC):
--------------------
1. searchInsertPos : O(1) → Only variables used
2. compute : O(1) extra space (sorting is in-place)
3. bisect.bisect_left : O(1)
'''
