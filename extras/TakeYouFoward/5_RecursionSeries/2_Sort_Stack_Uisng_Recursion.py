# Link: https://takeuforward.org/plus/dsa/problems/sort-a-stack

# Sort Stack using Recursion

def sortStack(stack: list[int]) -> list[int]:
    if len(stack) <= 1:
        return stack  # Return as is for base case

    # Step 1: Pop the top element
    top = stack.pop()

    # Step 2: Recursively sort the rest of the stack
    sortStack(stack)

    # Step 3: Insert the popped element in sorted order
    insert_sorted(stack, top)

    return stack  # Return the sorted stack

def insert_sorted(stack: list[int], element: int):
    # If stack is empty or element is greater than top, push it
    if not stack or element > stack[-1]:
        stack.append(element)
        return

    # Else pop the top, insert recursively, then push top back
    top = stack.pop()
    insert_sorted(stack, element)
    stack.append(top)


# Test
stack = [4, 1, 3, 2]
ans = sortStack(stack)
print(f'Sorted Stack: {ans}')  # Output: [4, 3, 2, 1]
