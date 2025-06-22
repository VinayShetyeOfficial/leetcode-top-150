# 71. Simplify Path (Medium)
# https://leetcode.com/problems/simplify-path

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []  # Holds the valid directory names
        curr = ""   # Temporarily builds the current dir name

        # Add an extra slash at the end to force final flush
        for c in path + "/":
            if c == "/":
                if curr == "..":
                    if stack:
                        stack.pop()  # Go back one directory
                elif curr and curr != ".":
                    stack.append(curr)  # Valid dir name
                curr = ""  # Reset for next segment
            else:
                curr += c  # Build the current dir name

        return "/" + "/".join(stack)

"""
✅ Time Complexity: O(n)
👉 n = length of input path (each char is processed once)

✅ Space Complexity: O(n)
👉 Stack stores directory names, worst case all dirs are valid
"""