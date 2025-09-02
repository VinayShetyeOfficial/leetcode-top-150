# Link: https://leetcode.com/problems/next-greater-element-i

# Next Greater Element

def nextLargerElement(arr):
    n = len(arr)
    result = [-1] * n
    
    for index in range(n):  # include last element also
        start = index + 1
        
        while start < n:
            if arr[start] > arr[index]:
                result[index] = arr[start]
                break
            start += 1
            
    return result


# ----------- Test Driver Code -----------
if __name__ == '__main__':
    arr = [3, 10, 4, 2, 1, 2, 6, 1, 7, 2, 9]
    ans = nextLargerElement(arr)
    print(f'Next Greater Element Result:\n{ans}')


"""
Time Complexity: O(n^2), where n is the number of elements in the array (nested loops)
Space Complexity: O(n), for the result array
"""
