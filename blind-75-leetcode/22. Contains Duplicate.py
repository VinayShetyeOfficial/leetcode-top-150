# Link: https://leetcode.com/problems/happy-number/description/

# ============================================
# Happy Number
# ============================================

class Solution(object):
    def isHappy(self, n):
        seen = set()  # To store numbers we've already seen to detect cycles
        
        while n != 1:
            # Compute the sum of squares of digits
            n = sum(int(digit)**2 for digit in str(n))
            # Uncomment below to see the sequence
            # print(n)
            
            # If we have seen this number before, a cycle exists → not happy
            if n in seen:
                return False
            seen.add(n)
        
        return True

"""
Time Complexity (TC): O(log n * log n)
- Each iteration computes sum of squares of digits (~log n digits),
- Number of iterations is bounded (will eventually repeat or reach 1).

Space Complexity (SC): O(log n)
- We store numbers seen in a set to detect cycles.
"""

# ============================================
# Driver Code
# ============================================

if __name__ == '__main__':
    obj = Solution()
    print("Is 10 a happy number?", obj.isHappy(10))  # Output: True
    print("Is 19 a happy number?", obj.isHappy(19))  # Output: True
    print("Is 2 a happy number?", obj.isHappy(2))    # Output: False
