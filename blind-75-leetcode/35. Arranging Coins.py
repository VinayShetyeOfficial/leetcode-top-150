# Link: https://leetcode.com/problems/arranging-coins/description/

# ============================================
# Solution 1: Binary Search (Efficient)
# ============================================
class Solution1:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n
        while left <= right:
            mid = (left + right) // 2
            coins_used = (mid * (mid + 1)) // 2  # Sum of first 'mid' natural numbers
            
            if coins_used == n:  # Perfect staircase
                return mid
            elif coins_used < n:  # Can still build more rows
                left = mid + 1
            else:  # Too many coins used, reduce search range
                right = mid - 1
                
        return right  # 'right' will be at the last valid row count

"""
Time Complexity: O(log n)
Space Complexity: O(1)
"""

# ============================================
# Solution 2: Iterative subtraction
# ============================================
class Solution2(object):
    def arrangeCoins(self, n):
        i = 1
        while n >= 0:
            n -= i
            i += 1
        return i - 1

"""
Time Complexity: O(sqrt(n))
Space Complexity: O(1)
"""

# ============================================
# Solution 3: Step counter method
# ============================================
class Solution3(object):
    def arrangeCoins(self, n):
        if n == 1:
            return n
        
        step = 0
        coins = 1
        
        while n > 0:
            n -= coins
            coins += 1
            
            if n >= 0:
                step += 1
            else:
                break
            
        return step

"""
Time Complexity: O(sqrt(n))
Space Complexity: O(1)
"""

# ============================================
# Driver Code
# ============================================
if __name__ == '__main__':
    n = 10

    obj1 = Solution1()
    print("Maximum full rows (Solution 1):", obj1.arrangeCoins(n))

    obj2 = Solution2()
    print("Maximum full rows (Solution 2):", obj2.arrangeCoins(n))

    obj3 = Solution3()
    print("Maximum full rows (Solution 3):", obj3.arrangeCoins(n))
