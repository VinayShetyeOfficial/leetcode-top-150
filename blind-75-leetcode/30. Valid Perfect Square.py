# Link: https://leetcode.com/problems/valid-perfect-square/description/

# Valid Perfect Square
class Solution(object):
    def sPerfectSquare(self, num):
        left, right = 1, num

        while left <= right:
            mid = (left + right)//2
            square = mid*mid

            if(square == num):
                return True
            elif square < num:
                left = mid + 1
            else:
                right = mid - 1

        return False
        # return math.floor(num**0.5)**2 == num          # ⭐ Optional 

    
# Driver code
if __name__ == '__main__':
    obj = Solution()
    num = 14
    print(obj.sPerfectSquare(num))