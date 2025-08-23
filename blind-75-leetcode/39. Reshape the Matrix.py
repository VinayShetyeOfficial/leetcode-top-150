# ============================================
# Reshape the Matrix - LeetCode
# ============================================
import itertools
import numpy as np

# ---------------------------
# Solution 1: Using itertools
# ---------------------------
class Solution1(object):
    def matrixReshape(self, mat, r, c):
        # Flatten the original matrix
        arr = list(itertools.chain(*mat))
        
        # Check if reshaping is possible
        if len(arr) != r * c:
            return mat
        
        result = []
        index = 0
        for i in range(r):
            temp = []
            for j in range(c):
                temp.append(arr[index])
                index += 1
            result.append(temp)
        return result

"""
Time Complexity (TC): O(m*n) 
   - m*n elements are iterated while flattening and reshaping
Space Complexity (SC): O(m*n) 
   - extra array 'arr' of size m*n + result matrix
"""

# ---------------------------
# Solution 2: List comprehension
# ---------------------------
class Solution2(object):
    def matrixReshape(self, mat, r, c):
        m, n = len(mat), len(mat[0])
        
        # Check if reshape is possible
        if m * n != r * c:
            return mat
        
        # Flatten the matrix and reshape
        flattened = [val for row in mat for val in row]
        reshaped = [flattened[i*c:(i+1)*c] for i in range(r)]
        return reshaped

"""
Time Complexity (TC): O(m*n)
   - flattening and slicing operations go through all elements once
Space Complexity (SC): O(m*n)
   - 'flattened' list of size m*n + reshaped list
"""

# ============================================
# Sub-steps / Utility Functions
# ============================================

# ⭐ Multi-dimensional array to 1D array (recursive)
def flatten_recursive(array):
    result = []
    for element in array:
        if isinstance(element, list):
            result.extend(flatten_recursive(element))
        else:
            result.append(element)
    return result

"""
Time Complexity (TC): O(N) 
   - N = total number of scalar elements
Space Complexity (SC): O(N) 
   - result list + recursive call stack depth (worst case O(N))
"""

# ⭐ Flatten using itertools
def flatten_itertools(array):
    return list(itertools.chain(*array))

"""
Time Complexity (TC): O(m*n) 
   - goes through all elements once
Space Complexity (SC): O(m*n)
   - creates new flattened list
"""

# ⭐ Flatten / reshape using NumPy
def flatten_numpy(array, r, c):
    arr = np.array(array)
    return arr.reshape((r*c, ))  # For 1D array

"""
Time Complexity (TC): O(m*n)
   - converting to NumPy array + reshaping
Space Complexity (SC): O(m*n)
   - NumPy stores data in a new array structure
"""

def reshape_numpy(array, r, c):
    arr = np.array(array)
    return arr.reshape((r, c))   # For reshaped 2D array

"""
Time Complexity (TC): O(m*n)
   - conversion + reshape
Space Complexity (SC): O(m*n)
   - new NumPy array structure
"""

# ============================================
# Driver Code
# ============================================
if __name__ == '__main__':
    mat1 = [[1,2],[3,4],[5,6],[7,8],[9]]
    mat2 = [[1,2], [3,4], [5,6], [7,8]]
    
    obj1 = Solution1()
    print("Solution1:", obj1.matrixReshape(mat1, 1, 9))
    
    obj2 = Solution2()
    print("Solution2:", obj2.matrixReshape(mat2, 2, 4))
    
    array_multid = [[1, 2, [3, 4]], [5, 6], [7, [8, 9]]]
    print("Flatten recursive:", flatten_recursive(array_multid))
    
    array_2d = [[1,2,3],[4,5,6],[7,8,9]]
    print("Flatten itertools:", flatten_itertools(array_2d))
    
    print("Flatten NumPy:", flatten_numpy(array_2d, 1, 9))
    print("Reshape NumPy:", reshape_numpy(array_2d, 3, 3))
