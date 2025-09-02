# Link: https://takeuforward.org/plus/dsa/problems/implement-queue-using-arrays

# Implement Queue using Arrays

class ArrayQueue:
    def __init__(self):
        """Initialize an empty queue"""
        self.queue = []

    def push(self, x: int) -> None:
        """Insert an element at the end of the queue"""
        self.queue.append(x)

    def pop(self) -> int:
        """Remove and return the front element of the queue"""
        if not self.isEmpty():
            return self.queue.pop(0)
        return None  # Optional: safe fallback

    def peek(self) -> int:
        """Return the front element without removing it"""
        if not self.isEmpty():
            return self.queue[0]
        return None  # Optional: safe fallback

    def size(self) -> int:
        """Return the number of elements in the queue"""
        return len(self.queue)

    def isEmpty(self) -> bool:
        """Check if the queue is empty"""
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


"""
Time Complexity:
- push(): O(1)
- pop(): O(n) (since list.pop(0) shifts all elements)
- peek(): O(1)
- size(): O(1)
- isEmpty(): O(1)

Space Complexity:
- O(n), where n is the number of elements stored in the queue
"""
