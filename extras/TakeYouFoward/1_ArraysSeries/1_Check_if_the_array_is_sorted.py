# Link: https://takeuforward.org/plus/dsa/problems/check-if-the-array-is-sorted-ii

# To check if number list is sorted or not [Ascending or Descending Order]

# Ascending order check
def isAscending(nums):
    for index in range(1, len(nums)):
        if nums[index - 1] > nums[index]:        # Check for instance where condition fails
            return False
    return True

# Descending order check
def isDescending(nums):
    for index in range(1, len(nums)):
        if nums[index - 1] < nums[index]:        # Check for instance where condition fails
            return False
    return True

# General function: Check if array is sorted (ascending or descending)
def isSorted(arr):
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1)) or \
           all(arr[i] >= arr[i+1] for i in range(len(arr)-1))


# Driver Code
if __name__ == '__main__':
    arr1 = [1, 2, 3, 4, 5]    # Ascending
    arr2 = [5, 4, 3, 2, 1]    # Descending
    arr3 = [1, 3, 2, 4]       # Not sorted
    arr4 = [7]                # Single element

    print(isAscending(arr1))  # True
    print(isDescending(arr2)) # True
    print(isSorted(arr3))     # False
    print(isSorted(arr4))     # True


'''
Special Case:
-------------
Single-element list [1] or empty list []

- len(arr) = 1 → range(len(arr) - 1) = range(0)
- Loop has zero iterations
- all([]) returns True (vacuous truth)
- Function returns True

Time Complexity (TC):
-------------------
- isAscending / isDescending: O(N)
- isSorted (with all()): O(N) for each check → worst case O(2N) ~ O(N)

Space Complexity (SC):
--------------------
- O(1) → No extra space used except for variables
'''
