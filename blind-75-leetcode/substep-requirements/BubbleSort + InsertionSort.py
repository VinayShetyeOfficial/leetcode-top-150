def bubbleSort(arr):
    n = len(arr)
    
    for i in range(n):
        swapped = False  # Flag to detect any swap
        
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True  # Swap happened
        
        if not swapped:
            break  # No swaps means array is sorted
    
    return arr

if __name__ == "__main__":
    arr = [6, 4, 7, 1, 2, 9, 5, 0, 8, 3]
    print("Sorted Array:", bubbleSort(arr))

=======================================================

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1

        arr[j + 1] = key
    
    return arr

	

    