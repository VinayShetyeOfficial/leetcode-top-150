# ============================================
# To Lower Case - LeetCode
# ============================================

# ---------------------------
# Solution 1: Manual conversion using ASCII values
# ---------------------------
class Solution1(object):
    def toLowerCase(self, s):
        result = ''
        for char in s:
            if 'A' <= char <= 'Z':
                # Converting uppercase to lowercase by adding the difference between 'a' and 'A'
                result += chr(ord(char) + (ord('a') - ord('A')))
            else:
                result += char
        return result

"""
Time Complexity (TC): O(n)
   - Traverse all characters in the string once
Space Complexity (SC): O(n)
   - New string 'result' is built of size n
"""

# ---------------------------
# Solution 2: Using Python built-ins (isupper / lower)
# ---------------------------
class Solution2(object):
    def toLowerCase(self, s):
        res = ""
        for c in s:
            if c.isupper():
                res += c.lower()
            else:
                res += c
        return res
        
        # Alternatively, the simplest one-liner:
        # return s.lower()

"""
Time Complexity (TC): O(n)
   - Each character is checked and possibly converted
Space Complexity (SC): O(n)
   - New string 'res' is created of size n
"""

# ============================================
# Sub-steps / Utility Demonstration
# ============================================

# Finding ASCII value of CHAR value
char = 'A'
ascii_value = ord(char)
print(f"The ASCII value of '{char}' is {ascii_value}")  # 65

# Finding CHAR value for ASCII value
ascii_value = 65
char = chr(ascii_value)
print(f"The character for ASCII value {ascii_value} is '{char}'")  # A

# ============================================
# Driver Code
# ============================================
if __name__ == '__main__':
    obj1 = Solution1()
    s1 = "al&phaBET"
    print("Solution1:", obj1.toLowerCase(s1))  # Output: "al&phabet"

    obj2 = Solution2()
    s2 = "Hello"
    print("Solution2:", obj2.toLowerCas
