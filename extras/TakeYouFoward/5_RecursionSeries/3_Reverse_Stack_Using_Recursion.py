# Link: https://takeuforward.org/plus/dsa/problems/reverse-a-stack

# Reverse Stack using Recursion

def reverseStack(stack: list[int]) -> list[int]:
    # Base case: if stack is empty, return empty list
    if not stack:
        return []

    # Step 1: Pop the top element
    top = stack.pop()

    # Step 2: Recursively reverse the remaining stack
    reversed_rest = reverseStack(stack)

    # Step 3: Append the top element at the end
    return reversed_rest + [top]


# Driver Code
if __name__ == '__main__':
    stack = [4, 1, 3, 2]
    ans = reverseStack(stack)
    print(f'Reversed Stack: {ans}')  # Output: [2, 3, 1, 4]


"""
Time Complexity (TC): O(n^2)
  -> Each recursive call creates a new list when concatenating: [reversed_rest + [top]].
Space Complexity (SC): O(n)
  -> Recursion stack depth is n.
"""