# ============================================
# Decrypt String from Alphabet to Integer Mapping - LeetCode
# ============================================

class Solution(object):
    def freqAlphabets(self, s):
        # Mapping for single digits '1' to '9'
        charSet1 = {str(i): chr(96 + i) for i in range(1, 10)}
        # Mapping for two digits with '#' '10#' to '26#'
        charSet2 = {str(i) + '#': chr(96 + i) for i in range(10, 27)}

        i = 0
        res = ""
        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == '#':
                res += charSet2[s[i:i+3]]
                i += 3
            else:
                res += charSet1[s[i]]
                i += 1
                
        return res

# ============================================
# Driver Code
# ============================================
if __name__ == '__main__':
    obj = Solution()
    s = "10#11#12"
    print(obj.freqAlphabets(s))  # Output: "jkab"

"""
Time Complexity (TC): O(n)
- We traverse the string once, so linear time with respect to string length n.

Space Complexity (SC): O(1)
- Dictionaries have fixed size (26 letters). Only result string uses extra space.
"""
