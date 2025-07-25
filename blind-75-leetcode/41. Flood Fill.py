# Link: https://leetcode.com/problems/flood-fill/description/

# Flood Fill
import numpy as np

class Solution(object):
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
            
# Driver code
if __name__ == '__main__':
    obj = Solution()
    
    sr = 1
    sc = 1
    color = 2
    image = [[1,1,1],[1,1,0],[1,0,1]]
    resultArr = np.array((obj.floodFill(image, sr, sc, color)))
    print(resultArr)
    


