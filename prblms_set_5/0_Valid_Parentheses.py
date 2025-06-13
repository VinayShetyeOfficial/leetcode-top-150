# 20. Valid Parentheses (Easy) - Done
# https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        """
        Checks if a string containing brackets is valid.
        Uses a stack to match open and close brackets.
        """

        # Mapping of closing brackets to their corresponding opening brackets
        bracket_map = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            if char in bracket_map:
                # If top of the stack matches the corresponding opening bracket, pop it
                if stack and stack[-1] == bracket_map[char]:
                    stack.pop()
                else:
                    return False  # Mismatch or stack is empty
            else:
                # Push opening brackets onto the stack
                stack.append(char)

        # If stack is empty, all brackets were matched properly
        return not stack
    
"""
✅ Time Complexity: O(n)
👉 One pass through the string

✅ Space Complexity: O(n)
👉 Stack may store up to n/2 opening brackets
"""

