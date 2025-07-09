# Link: https://leetcode.com/problems/happy-number/description/

# Happy Number 
class Solution(object):
    def isHappy(self, n):
        temp = []
        
        while n != 1:
            n = sum([int(i)**2 for i in str(n)])
            print(n)
            if n in temp:
                return False
            else:
                temp += [n]
        
        return True

# Driver code        
if __name__ == '__main__':
    obj = Solution()
    print(obj.isHappy(10))