# Link: https://leetcode.com/problems/check-if-it-is-a-straight-line/description/

# Check If It Is a Straight Line
class Solution(object):
    def checkStraightLine(self, coordinates):
        
        (x0, y0), (x1, y1) = coordinates[:2]
        dx, dy = x1 - x0, y1 - y0
    
        for x, y in coordinates[2:]:
            if (y - y0) * dx != (x - x0) * dy:
                return False
    
        return True
        
# Driver code
if __name__ == '__main__':
    obj = Solution()
    coordinates = [[0,0],[0,1],[0,-1]]
    print(obj.checkStraightLine(coordinates))
    