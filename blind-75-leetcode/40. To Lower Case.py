# Links: https://leetcode.com/problems/to-lower-case/

# To Lower Case
class Solution(object):
    def toLowerCase(self, s):
        result = ''
        for char in s:
            if 'A' <= char <= 'Z':
                # Converting uppercase to lowercase by adding the difference between 'a' and 'A'
                result += chr(ord(char) + (ord('a') - ord('A')))
            else:
                result += char
        return result
        
# Driver code
if __name__ == '__main__':
    obj = Solution()
    s = "al&phaBET"
    print(obj.toLowerCase(s))


# ----------------------

# Another Solution
class Solution(object):
    def toLowerCase(self, s):
        res = ""
        
        for c in s:
            if c.isupper():
                res += c.lower()
            else:
                res += c
        
        return res
        # return s.lower()       # Optional
        
# Driver code
if __name__ == '__main__':
    obj = Solution()
    s = "Hello"
    print(obj.toLowerCase(s))


# ----------------------

# ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐
# ====================== #
# Sub-steps Requirements #
# ====================== #

# Finding ASCII value of CHAR value
char = 'A'
ascii_value = ord(char)
print(f"The ASCII value of '{char}' is {ascii_value}") # 65

# Finding CHAR value for ASCII value
ascii_value = 65
char = chr(ascii_value)
print(f"The character for ASCII value {ascii_value} is '{char}'") # A