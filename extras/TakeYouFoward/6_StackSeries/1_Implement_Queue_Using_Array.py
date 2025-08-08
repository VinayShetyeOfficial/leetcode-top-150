# Link: https://takeuforward.org/plus/dsa/problems/implement-queue-using-arrays

# Implement Queue using Arrays

class ArrayQueue:
    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        if not self.isEmpty():
            return self.queue.pop(0)
        return None  # Optional: safe fallback

    def peek(self) -> int:
        if not self.isEmpty():
            return self.queue[0]
        return None  # Optional: safe fallback

    def size(self) -> int:
        return len(self.queue)

    def isEmpty(self) -> bool:
        return len(self.queue) == 0


if __name__ == '__main__':
    queue = ArrayQueue()
    queue.push(10)
    queue.push(20)
    queue.push(30)
    queue.push(40)
    queue.push(50)

    print(f'Queue: {queue.queue}')
    print(f'Popped Element: {queue.pop()}')
    print(f'Front Element: {queue.peek()}')
    print(f'Queue Size: {queue.size()}')
    print(f'Is Queue Empty: {queue.isEmpty()}')

    print()

    print(f'Queue: {queue.queue}')
    print(f'Popped Element: {queue.pop()}')
    print(f'Front Element: {queue.peek()}')
    print(f'Queue Size: {queue.size()}')
    print(f'Is Queue Empty: {queue.isEmpty()}')
