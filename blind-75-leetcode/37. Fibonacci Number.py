# Link: https://leetcode.com/problems/fibonacci-number/description/

# Fibonacci Number
# ⭐ Solution 1
class Solution(object):
    def fib(self, n):
        res = []
        
        for i in range(0, n+1):
            if i == 0:
                res += [0]
            elif i == 1:
                res += [1]
            else:
                res += [res[i-1] + res[i-2]]
                
        return res[n]
    
# Driver code
if __name__ == '__main__':
    obj = Solution()
    n = 9
    print(obj.fib(n))


# ----------------------

# Another Solution
class Solution(object):
    def fib(self, n):
        if n < 2:
            return n
        
        return self.fib(n-1) + self.fib(n-2)   # Recusion
    
# Driver code
if __name__ == '__main__':
    obj = Solution()
    n = 10
    print(obj.fib(n))

