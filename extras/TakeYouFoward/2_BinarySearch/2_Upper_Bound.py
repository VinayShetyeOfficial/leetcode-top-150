# Link: https://takeuforward.org/plus/dsa/problems/upper-bound

# Upper Bound

# Note: We must return index of 1st number greater than target, else array size

def upperBound(arr: list[int], target: int) -> int:
    low, high = 0, len(arr) - 1
    ans = len(arr)
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] > target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
            
    return ans
    # Note: If no answer is found, we return size of the array, hence initially ans = len(arr)

if __name__ == "__main__":
    arr = [3, 5, 8, 9, 15, 19]
    target = 9
    indx = upperBound(arr, target)
    print("The upper bound is the index:", indx)


"""
Time Complexity (TC): O(log N) -> binary search over the array
Space Complexity (SC): O(1) -> constant extra space used
"""
