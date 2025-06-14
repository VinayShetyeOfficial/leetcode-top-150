# 150. Evaluate Reverse Polish Notation (Medium)
# https://leetcode.com/problems/evaluate-reverse-polish-notation

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == '+':
                stack.append(stack.pop() + stack.pop())
            elif c == '-':
                num1, num2 = stack.pop(), stack.pop()
                stack.append(num2 - num1)
            elif c == '*':
                stack.append(stack.pop() * stack.pop())
            elif c == '/':
                num1, num2 = stack.pop(), stack.pop()
                stack.append(int(num2/num1))
            else:
                stack.append(int(c))
        return stack[0]

"""
✅ Time Complexity: O(n)
  - Each token is processed once

✅ Space Complexity: O(n)
  - Stack may grow to the number of tokens in the worst case
"""