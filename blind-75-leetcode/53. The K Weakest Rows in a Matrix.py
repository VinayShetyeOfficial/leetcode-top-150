# ============================================
# The K Weakest Rows in a Matrix - LeetCode
# ============================================

class Solution(object):
    def kWeakestRows(self, mat, k):
        # Compute row strength as (sum of 1's, row index)
        row_strength = [(sum(row), i) for i, row in enumerate(mat)]
        # Example: [(2, 0), (4, 1), (1, 2), (2, 3), (5, 4)]

        # Sort by strength first, then by index
        row_strength.sort()
        # Sorted: [(1, 2), (2, 0), (2, 3), (4, 1), (5, 4)]

        # Extract indices of first k weakest rows
        weakest_rows = [index for strength, index in row_strength[:k]]

        return weakest_rows

# ============================================
# Driver Code
# ============================================
if __name__ == '__main__':
    obj = Solution()
    mat = [
        [1,1,0,0,0],
        [1,1,1,1,0],
        [1,0,0,0,0],
        [1,1,0,0,0],
        [1,1,1,1,1]
    ]
    k = 3
    print(obj.kWeakestRows(mat, k))  # Output: [2, 0, 3]

"""
Time Complexity (TC): O(m * n + m log m)
- m: number of rows, n: number of columns
- O(m*n) for computing sum of each row
- O(m log m) for sorting rows

Space Complexity (SC): O(m)
- Extra space used to store row_strength list
"""
