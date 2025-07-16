# Maximum Nesting Depth of the Parentheses

def maxDepth(s: str) -> int:
    max_depth, current_depth = 0, 0
    
    for char in s:
        if char == '(':
            current_depth += 1
            max_depth = max(max_depth, current_depth)
        elif char == ')':
            current_depth -= 1
            
    return max_depth
    

# Example usage:
if __name__ == '__main__':
    s = "(1+(2*3)+((8)/4))+1"
    ans = maxDepth(s)
    print(f'Max Depth Of Parenthesis: {ans}')
    