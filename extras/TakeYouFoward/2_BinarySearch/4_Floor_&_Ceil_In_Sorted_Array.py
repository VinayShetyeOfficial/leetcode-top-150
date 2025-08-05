# Link: https://takeuforward.org/plus/dsa/problems/floor-and-ceil-in-sorted-array

# Floor and Ceil in Sorted Array

def findFloorCeil(nums, x):
    n = len(nums)
    floor, ceil = -1, -1

    # Floor: largest <= x
    low, high = 0, n - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] <= x:
            floor = nums[mid]
            low = mid + 1
        else:
            high = mid - 1

    # Ceil: smallest >= x
    low, high = 0, n - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] >= x:
            ceil = nums[mid]
            high = mid - 1
        else:
            low = mid + 1

    return floor, ceil

# Example usage:
if __name__ == "__main__":
    nums = [3, 4, 4, 7, 8, 10]
    x = 5
    fl, ce = findFloorCeil(nums, x)
    print(fl, ce)  # Output: 4 7

















