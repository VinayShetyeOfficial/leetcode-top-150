# Link: https://leetcode.com/problems/reshape-the-matrix/description/

# Reshape the Matrix
import itertools

class Solution(object):
    def matrixReshape(self, mat, r, c):
        # Flattening the original matrix
        arr = list(itertools.chain(*mat))
        
        # Checking if reshaping is possible
        if len(arr) != r * c:
            return mat
        
        result = []
        index = 0
        for i in range(r):
            temp = []
            for j in range(c):
                temp += [arr[index]]
                index += 1
                
            result.append(temp)
            
        return result
            
# Driver code
if __name__ == '__main__':
    obj = Solution()
    r = 1
    c = 9
    mat = [[1,2],[3,4],[5,6], [7,8], [9]]

    print(obj.matrixReshape(mat, r, c))


# ----------------------

# Another Solution
class Solution(object):
    def matrixReshape(self, mat, r, c):
        m, n = len(mat), len(mat[0])
        
        # Check if reshape is possible
        if m * n != r * c:
            return mat
        
        # Flatten the matrix and reshape it
        flattened = [val for row in mat for val in row]
        reshaped = [flattened[i*c:(i+1)*c] for i in range(r)]
        
        return reshaped
            
# Driver code
if __name__ == '__main__':
    obj = Solution()
    r = 2
    c = 4
    mat = [[1,2], [3,4], [5,6], [7,8]]

    print(obj.matrixReshape(mat, r, c))


# ====================== #
# Sub-steps Requirements #
# ====================== #
# ⭐ Multi-dimensional Array to 1D Array
def flatten(array):
    result = []
    
    for element in array:
        if isinstance(element, list):
           result.extend(flatten(element))
        else:
            result.append(element)
    
    return result

#Multidimensional Array to 1D Array
array_multid = [[1, 2, [3, 4]], [5, 6], [7, [8, 9]]]

print(flatten(array_multid))

# ----------------------
# Using inbuilt-functions
# ⭐ 2D Array to 1D Array
import itertools

def flatten(array):
    
    result_array = list(itertools.chain(*array))
    
    return result_array

# Multidimensional Array to 1D Array
array_2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(flatten(array_2d))


# ⭐ 2D Array to 1D Array using Numpy Methods
import numpy as np

r = 1
c = 9
array_2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

array = np.array(array_2d)

# Reshape to a 1D array
array = array.reshape((r*c, ))         # <======== Note [for 1 row array] ========
print(array)
# Output: [1 2 3 4 5 6 7 8 9]

# ----------------------

# ⭐ 2D Array to 1D Array using Numpy Methods
import numpy as np

r = 3
c = 3
array_2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

array = np.array(array_2d)

# Reshape to a 1D array
array = array.reshape((r, c))         # <======== Note [for 1+ row array] ========
print(array)
# Output: [1 2 3 4 5 6 7 8 9]

