# Link: https://takeuforward.org/plus/dsa/problems/maximum-nesting-depth-of-the-parentheses

# Maximum Nesting Depth of Parentheses in a string

def maxDepth(s: str) -> int:
    max_depth = 0
    current_depth = 0

    for char in s:
        if char == '(':
            current_depth += 1
            max_depth = max(max_depth, current_depth)
        elif char == ')':
            current_depth -= 1

    return max_depth

# Example usage
if __name__ == '__main__':
    s = "(1+(2*3)+((8)/4))+1"
    ans = maxDepth(s)
    print(f'Maximum Nesting Depth of Parentheses: {ans}')  # Output: 3
