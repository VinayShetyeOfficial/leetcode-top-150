# ============================================
# N-th Tribonacci Number - LeetCode
# ============================================

class Solution:
    def tribonacci(self, n: int) -> int:
        # Base cases
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        
        # Initialize first three Tribonacci numbers
        t0, t1, t2 = 0, 1, 1
        
        # Iteratively compute Tribonacci numbers
        for _ in range(3, n + 1):
            t_next = t0 + t1 + t2
            t0, t1, t2 = t1, t2, t_next  # Shift numbers
        
        return t2

# ============================================
# Driver Code
# ============================================
if __name__ == '__main__':
    obj = Solution()
    n = 25
    print(obj.tribonacci(n))  # Output: 1389537

"""
Time Complexity (TC): O(n)
- Loop runs from 3 to n, so linear time.

Space Complexity (SC): O(1)
- Only 3 variables (t0, t1, t2) are used to store previous Tribonacci numbers.
"""
