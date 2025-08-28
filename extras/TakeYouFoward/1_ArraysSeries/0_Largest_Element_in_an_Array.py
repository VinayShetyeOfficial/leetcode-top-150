# Link: https://takeuforward.org/plus/dsa/problems/largest-element

# Largest Element in an Array

import random

# Find Largest Element in Array
def findLargest(nums: list[int]) -> int:
    """
    Returns the largest element in the array
    """
    if not nums:
        return None  # Edge case: empty list

    largestNum = nums[0]  # Initialize largest with first element

    for num in nums:
        if num > largestNum:
            largestNum = num
            
    return largestNum


# Find Second-Largest and Second-Smallest Element in Array
def findSecondElements(nums: list[int]) -> tuple[int, int]:
    """
    Returns a tuple (second_smallest, second_largest)
    """
    smallest = second_smallest = float('inf')
    largest = second_largest = float('-inf')
    
    for num in nums:
        # Update smallest and second smallest
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif smallest < num < second_smallest:
            second_smallest = num

        # Update largest and second largest
        if num > largest:
            second_largest = largest
            largest = num
        elif largest > num > second_largest:
            second_largest = num

    return (second_smallest, second_largest)


# Driver Code
if __name__ == '__main__':
    arr = [random.randint(1, 100) for _ in range(10)]
    print("Array:", arr)

    largest = findLargest(arr)
    print("Largest Element:", largest)

    second_smallest, second_largest = findSecondElements(arr)
    print("Second Smallest:", second_smallest)
    print("Second Largest:", second_largest)


# Time Complexity (TC):
# - findLargest: O(N) -> Traverse all elements once
# - findSecondElements: O(N) -> Traverse all elements once
# Space Complexity (SC):
# - O(1) -> Constant extra space, no extra arrays used
