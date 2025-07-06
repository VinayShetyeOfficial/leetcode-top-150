# Link: https://leetcode.com/problems/valid-parentheses/description/\

# Valid Parentheses
class Solution(object):
    def isValid(self, s):
        hashmap = {
            ")":"(",
            "]":"[",
            "}":"{"
        }

        stack = []

        for c in s:

            if c in hashmap:
                if stack and stack[-1]==hashmap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return not stack

# Driver code
if __name__ == "__main__":
    obj = Solution()
    s = "({}[])"
    print(obj.isValid(s))