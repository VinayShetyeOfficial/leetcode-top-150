# Add Binary
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ''
        carry = 0

        # Reverse the two strings for easier left-to-right processing
        a, b = a[::-1], b[::-1]

        # Loop through the longer of the two strings
        for i in range(max(len(a), len(b))):    
            digitA = int(a[i]) if i < len(a) else 0
            digitB = int(b[i]) if i < len(b) else 0

            total = digitA + digitB + carry
            result = str(total % 2) + result  # Add the current binary digit
            carry = (total // 2)              # Update the carry

        if carry:
            result = '1' + result

        return result

"""
Time Complexity (TC): O(max(n, m)) 
- n = length of a, m = length of b
- We loop through both strings once.

Space Complexity (SC): O(max(n, m)) 
- Result string stores at most max(n, m) + 1 characters.
"""
