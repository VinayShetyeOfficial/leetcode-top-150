# Link: https://leetcode.com/problems/fibonacci-number/description/

# ============================================
# Solution 1: Iterative (Bottom-up)
# ============================================
class Solution1(object):
    def fib(self, n):
        res = []
        
        for i in range(0, n + 1):
            if i == 0:
                res.append(0)
            elif i == 1:
                res.append(1)
            else:
                res.append(res[i - 1] + res[i - 2])
                
        return res[n]

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""

# ============================================
# Solution 2: Recursive
# ============================================
class Solution2(object):
    def fib(self, n):
        if n < 2:
            return n
        return self.fib(n - 1) + self.fib(n - 2)

"""
Time Complexity: O(2^n)
Space Complexity: O(n) recursion stack
"""

# ============================================
# Driver Code
# ============================================
if __name__ == '__main__':
    n1 = 9
    obj1 = Solution1()
    print("Fibonacci Number (Iterative) for n =", n1, "is", obj1.fib(n1))

    n2 = 10
    obj2 = Solution2()
    print("Fibonacci Number (Recursive) for n =", n2, "is", obj2.fib(n2))
