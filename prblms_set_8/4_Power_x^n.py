# 50. Pow(x, n) (Medium)
# https://leetcode.com/problems/powx-n

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if x == 0: return 0        # edge case
            if n == 0: return 1        # base case

            res = helper(x, n // 2)    # divide the problem
            res *= res                 # combine results
            return x * res if n % 2 else res  # handle odd powers

        res = helper(x, abs(n))        # always call helper with positive power
        return res if n >= 0 else 1 / res  # if original n was negative, take reciprocal


"""
✅ Time Complexity: O(log n)
We divide n by 2 in every recursive call.

✅ Space Complexity: O(log n)
Due to recursive stack.
"""
