# Link: https://takeuforward.org/plus/dsa/problems/implement-stack-using-arrays

# Implement Stack using Array

class ArrayStack:
    def __init__(self):
        """Initialize an empty stack using a list"""
        self.stack = []
    
    def push(self, x: int) -> None:
        """Push element onto the stack"""
        self.stack.append(x)

    def pop(self) -> int:
        """Remove and return the top element from the stack"""
        if not self.isEmpty():
            return self.stack.pop()
        return None  # Return None if stack is empty

    def top(self) -> int:
        """Return the top element without removing it"""
        if not self.isEmpty():
            return self.stack[-1]
        return None  # Return None if stack is empty

    def size(self) -> int:
        """Return current size of stack"""
        return len(self.stack)

    def isEmpty(self) -> bool:
        """Check whether the stack is empty"""
        return len(self.stack) == 0


if __name__ == '__main__':
    stack = ArrayStack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    stack.push(50)

    print(f'Stack: {stack.stack}')
    print(f'Popped Element: {stack.pop()}')
    print(f'Top Element: {stack.top()}')
    print(f'Stack Size: {stack.size()}')
    print(f'Is Stack Empty: {stack.isEmpty()}')
    
    print(f'Stack: {stack.stack}')
    print(f'Popped Element: {stack.pop()}')
    print(f'Top Element: {stack.top()}')
    print(f'Stack Size: {stack.size()}')
    print(f'Is Stack Empty: {stack.isEmpty()}')

"""
Time Complexity:
- push(x): O(1)
- pop(): O(1)
- top(): O(1)
- size(): O(1)
- isEmpty(): O(1)

Space Complexity:
- O(N), where N is the number of elements in the stack
"""
