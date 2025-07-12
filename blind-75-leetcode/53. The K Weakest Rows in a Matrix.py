# Link: https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/description/

# The K Weakest Rows in a Matrix
class Solution(object):
    def kWeakestRows(self, mat, k):
        row_strength = [(sum(row), i) for i, row in enumerate(mat)]
        # Row Strength:  [(2, 0), (4, 1), (1, 2), (2, 3), (5, 4)]

        row_strength.sort()
        # Row Strength (Sorted):  [(1, 2), (2, 0), (2, 3), (4, 1), (5, 4)]

        weakest_rows = [index for strength, index in row_strength[:k]]
        # [2, 0, 3]

        return weakest_rows
        
# Driver code
if __name__ == '__main__':
    obj = Solution()
    mat = [[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]] 
    k = 3
    print(obj.kWeakestRows(mat, k))
    