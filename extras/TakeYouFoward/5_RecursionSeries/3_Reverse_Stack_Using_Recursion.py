# Reverse Stack using recursion

def reverseStack(stack: list[int]) -> list[int]:
    if not stack:
        return []

    top = stack.pop()
    reversed_rest = reverseStack(stack)
    return [top] + reversed_rest

# Test
stack = [4, 1, 3, 2]
ans = reverseStack(stack)
print(f'Reversed Stack: {ans}')    # Outut: [2, 3, 1, 4]
