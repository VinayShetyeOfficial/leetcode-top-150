# Linear Search

def binarySearch(nums: list[int], target: int) -> int:
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
    print(f'Index: {binarySearch(arr, target)}')  # Output: 4
