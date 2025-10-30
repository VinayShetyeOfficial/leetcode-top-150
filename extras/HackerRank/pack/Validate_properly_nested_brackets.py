# https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/validate-properly-nested-brackets

def areBracketsProperlyMatched(code_snippet):
    # Write your code here
    stack = []
    bracketMap = {')':'(','}':'{', ']':'['}
    
    for char in code_snippet:
        if char in bracketMap:
            if stack and stack[-1] == bracketMap[char]:
                stack.pop()
            else:
                return 0
        else:
            if char in bracketMap.values():
                stack.append(char)
           
    return 1 if not stack else 0

