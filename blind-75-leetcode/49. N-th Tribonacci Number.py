# Link: https://leetcode.com/problems/n-th-tribonacci-number/description/

# N-th Tribonacci Number
class Solution(object):
    def tribonacci(self, n):
        res = []
        
        for i in range(0, n+2):
            if i == 0:
                res += [0]
            elif i == 1:
                res += [1]
            elif i == 2:
                res += [1]
            else:
                res += [res[i-1] + res[i-2] + res[i-3]]
        
        return res[n]
        
# Driver code
if __name__ == '__main__':
    obj = Solution()
    n = 25
    print(obj.tribonacci(n))
    