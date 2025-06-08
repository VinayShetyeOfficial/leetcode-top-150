# 202. Happy Number (Easy)
# https://leetcode.com/problems/happy-number

class Solution:
    def isHappy(self, n: int) -> bool:
        """
        Determines if a number is a happy number.
        Uses a set to detect cycles and avoid infinite loops.
        """
        seen = set()

        while n != 1:
            if n in seen:
                return False  # Cycle detected
            seen.add(n)

            # Replace n with the sum of squares of its digits
            n = sum(int(digit) ** 2 for digit in str(n))

        return True

"""
✅ Time Complexity: O(log n)
👉 Because each digit is squared and summed, the number size reduces over time

✅ Space Complexity: O(log n)
👉 For storing the set of previously seen values (at most logarithmic to n)
"""