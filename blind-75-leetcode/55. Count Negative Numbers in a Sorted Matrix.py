# Link: https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/description/

# Count Negative Numbers in a Sorted Matrix
class Solution(object):
    def countNegatives(self, grid):
        count = 0
        for row in grid:
            for num in row:
                if num < 0:
                    count += 1
        return count
        
# Driver code
if __name__ == '__main__':
    obj = Solution()
    grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
    print(obj.countNegatives(grid))
