# ============================================
# Flood Fill - LeetCode
# ============================================

from typing import List
import numpy as np

# ---------------------------
# Solution 1: Recursive DFS
# ---------------------------
class Solution1:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS, COLS = len(image), len(image[0])
        originalColor = image[sr][sc]

        if originalColor == color:
            return image

        def fill(i, j):
            if (i < 0 or i >= ROWS or j < 0 or j >= COLS or image[i][j] != originalColor):
                return

            image[i][j] = color

            fill(i + 1, j)
            fill(i - 1, j)
            fill(i, j + 1)
            fill(i, j - 1)

        fill(sr, sc)
        return image

"""
Time Complexity (TC): O(m*n)
   - In worst case, all pixels are connected and need to be visited once
Space Complexity (SC): O(m*n)
   - Recursion stack can go as deep as all pixels in worst case
"""

# ---------------------------
# Solution 2: Recursive DFS with bounds check helper
# ---------------------------
class Solution2(object):
    def withinBounds(self, i, j, m, n):
        return 0 <= i < m and 0 <= j < n
    
    def floodFill(self, image, sr, sc, color):
        m, n = len(image), len(image[0])
        original_color = image[sr][sc]
        
        if original_color == color:
            return image
        
        def fill(i, j):
            if self.withinBounds(i, j, m, n) and image[i][j] == original_color:
                image[i][j] = color
                fill(i-1, j)  # Top
                fill(i+1, j)  # Bottom
                fill(i, j-1)  # Left
                fill(i, j+1)  # Right
        
        fill(sr, sc)
        return image

"""
Time Complexity (TC): O(m*n)
   - Same as Solution1, every pixel might be visited once
Space Complexity (SC): O(m*n)
   - Recursion stack depth worst case = total pixels
"""

# ============================================
# Driver Code
# ============================================
if __name__ == '__main__':
    # Test Solution1
    obj1 = Solution1()
    sr = 1
    sc = 1
    color = 2
    image1 = [[1,1,1],[1,1,0],[1,0,1]]
    result1 = obj1.floodFill(image1, sr, sc, color)
    print("Solution1 Result:")
    print(np.array(result1))
    
    # Test Solution2
    obj2 = Solution2()
    image2 = [[1,1,1],[1,1,0],[1,0,1]]
    result2 = obj2.floodFill(image2, sr, sc, color)
    print("Solution2 Result:")
    print(np.array(result2))
