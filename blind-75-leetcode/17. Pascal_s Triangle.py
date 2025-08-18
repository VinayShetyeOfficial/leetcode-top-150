# Link: https://leetcode.com/problems/pascals-triangle/

# ============================================
# Pascal's Triangle
# ============================================

class Solution(object):
    def generate(self, numRows):
        result = []
        
        for i in range(numRows):
            # Initialize row with 1s
            row = [1] * (i + 1)
            
            # Fill middle values using the previous row
            for j in range(1, i):
                row[j] = result[i - 1][j - 1] + result[i - 1][j]
            
            result.append(row)
        
        return result

"""
Time Complexity (TC): O(numRows^2)
- We generate each row and compute elements using previous row.

Space Complexity (SC): O(numRows^2)
- Result stores all rows of Pascal's Triangle.
"""

# ============================================
# Driver Code
# ============================================
if __name__ == '__main__':
    obj = Solution()
    numRows = 5
    print("Pascal's Triangle with", numRows, "rows:")
    print(obj.generate(numRows))
    # Output:
    # [
    #  [1],
    #  [1,1],
    #  [1,2,1],
    #  [1,3,3,1],
    #  [1,4,6,4,1]
    # ]
