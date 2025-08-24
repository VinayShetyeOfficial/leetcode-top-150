# ============================================
# Check If It Is a Straight Line - LeetCode
# ============================================

class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        # Take first two points
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        
        dx, dy = x1 - x0, y1 - y0  # Slope components (rise/run)
        
        # Check if all other points lie on the same line
        for x, y in coordinates[2:]:
            if (y - y0) * dx != (x - x0) * dy:  # Cross-multiplication avoids division
                return False
        
        return True

# ============================================
# Driver Code
# ============================================
if __name__ == '__main__':
    obj = Solution()
    coordinates = [[0,0], [0,1], [0,-1]]
    print(obj.checkStraightLine(coordinates))  # Output: True

"""
Time Complexity (TC): O(n)
- Loop through all points once, where n is the number of coordinates.

Space Complexity (SC): O(1)
- Only a few variables are used to store slopes and coordinates differences.
"""
