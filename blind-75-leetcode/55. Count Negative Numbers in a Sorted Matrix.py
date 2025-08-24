# ============================================
# Count Negative Numbers in a Sorted Matrix - LeetCode
# ============================================

from typing import List

# Optimized Approach (Using the sorted property)
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        index = COLS - 1
        pos = 0  # count of non-negative numbers
        
        for row in range(ROWS):
            # move left while negative numbers exist
            while index >= 0 and grid[row][index] < 0:
                index -= 1
            pos += index + 1  # count non-negative numbers in this row
        
        res = ROWS * COLS - pos  # total negatives
        return res

# Brute-force Approach
class SolutionBF(object):
    def countNegatives(self, grid):
        count = 0
        for row in grid:
            for num in row:
                if num < 0:
                    count += 1
        return count

# ============================================
# Driver Code
# ============================================
if __name__ == '__main__':
    obj = Solution()
    grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
    print(obj.countNegatives(grid))  # Output: 8

"""
Time Complexity (TC):
- Optimized: O(m + n)  -> m rows, n cols, move left at most n times
- Brute-force: O(m * n)

Space Complexity (SC):
- Both approaches: O(1) (ignoring input space)
"""
