# ============================================
# Bubble Sort and Insertion Sort
# ============================================

from typing import List

# Approach 1: Bubble Sort
def bubbleSort(arr: List[int]) -> List[int]:
    n = len(arr)
    
    for i in range(n):
        swapped = False  # Flag to detect any swap
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True  # Swap happened
        
        if not swapped:  # No swaps means array already sorted
            break
    
    return arr


# Approach 2: Insertion Sort
def insertionSort(arr: List[int]) -> List[int]:
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
    
    return arr


# ============================================
# Driver Code
# ============================================
if __name__ == "__main__":
    arr1 = [6, 4, 7, 1, 2, 9, 5, 0, 8, 3]
    print("Bubble Sort Result:", bubbleSort(arr1))

    arr2 = [6, 4, 7, 1, 2, 9, 5, 0, 8, 3]
    print("Insertion Sort Result:", insertionSort(arr2))


"""
Time Complexity (TC):
- Bubble Sort: 
    Worst & Average: O(n^2)
    Best Case (already sorted): O(n)
- Insertion Sort:
    Worst & Average: O(n^2)
    Best Case (already sorted): O(n)

Space Complexity (SC):
- Both Bubble Sort and Insertion Sort: O(1)  (In-place sorting)
"""
