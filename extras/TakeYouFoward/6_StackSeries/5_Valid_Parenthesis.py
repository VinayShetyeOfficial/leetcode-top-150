# Valid Parenthesis

def isValid(str: str) -> bool:
    bracket_map = {'}': '{', ')': '(', ']': '['}
    stack = []
    for bracket in str:
        if bracket in bracket_map:
            if stack and stack[-1] == bracket_map[bracket]:
                stack.pop()
            else:
                return False
        else:
            stack.append(bracket)

    return not stack


# ----------- Test Driver Code -----------
if __name__ == '__main__':
    test_cases = [
        '[([([{[()]}])])]',    # ✅ Valid
        '()[]{}',              # ✅ Valid
        '([{}])',              # ✅ Valid
        ')(',                  # ❌ Invalid
        '([)]',                # ❌ Invalid
        '{[}',                 # ❌ Invalid
        '',                    # ✅ Empty string is valid
        '[{()}([])]',          # ✅ Valid
        '[[[[[]]]]]',          # ✅ Valid
        '[[[[[[]]]]',          # ❌ One bracket missing
        '[(])',                # ❌ Wrong order
    ]

    for i, case in enumerate(test_cases):
        result = isValid(case)
        print(f'Test {i+1}: "{case}" → {result}')
