# Link: https://takeuforward.org/plus/dsa/problems/implement-stack-using-arrays

# Implement Stack using Array

class ArrayStack:
    def __init__(self):
        self.stack = []
    
    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if not self.isEmpty():
            return self.stack.pop()
        return None  # Optional: handle empty pop safely

    def top(self) -> int:
        if not self.isEmpty():
            return self.stack[-1]
        return None  # Optional: handle empty top safely

    def size(self) -> int:
        return len(self.stack)

    def isEmpty(self) -> bool:
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

