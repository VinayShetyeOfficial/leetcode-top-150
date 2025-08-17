# Link: https://leetcode.com/problems/valid-parentheses/description/

# Valid Parentheses
class Solution(object):
    def isValid(self, s):
        hashmap = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        stack = []

        for c in s:
            if c in hashmap:
                # If stack not empty and last element matches
                if stack and stack[-1] == hashmap[c]:
                    stack.pop()
                else:
                    return False
            else:
                # Push opening brackets
                stack.append(c)

        return not stack


# Driver code
if __name__ == "__main__":
    obj = Solution()
    s = "({}[])"
    print(obj.isValid(s))   # Expected: True

"""
===========================================
Time Complexity (TC): O(n)
- We iterate through each character of the string once (n = length of s).
- Stack operations (push/pop) take O(1).

Space Complexity (SC): O(n)
- In the worst case (all opening brackets), the stack grows to size n.
===========================================
"""
