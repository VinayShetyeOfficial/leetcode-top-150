# Link: https://takeuforward.org/plus/dsa/problems/implement-queue-using-stack

# Implement Queue using Two Stacks

class QueueUsingStacks:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, x):
        self.in_stack.append(x)

    def dequeue(self):
        if self.isEmpty():
            return None
        self._transfer_if_needed()
        return self.out_stack.pop()

    def peek(self):
        if self.isEmpty():
            return None
        self._transfer_if_needed()
        return self.out_stack[-1]

    def isEmpty(self):
        return not self.in_stack and not self.out_stack

    def _transfer_if_needed(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())


# ----------- Test Driver Code -----------
if __name__ == '__main__':
    queue = QueueUsingStacks()

    print("Enqueuing Elements: 10, 20, 30, 40, 50, 60")
    for val in [10, 20, 30, 40, 50, 60]:
        queue.enqueue(val)

    print(f"\nFront Element: {queue.peek()}")
    print(f"Dequeued Element: {queue.dequeue()}")
    print(f"Front Element after Dequeue: {queue.peek()}")
    print(f"Is Queue Empty?: {queue.isEmpty()}")

    print("\nDequeuing remaining elements:")
    while not queue.isEmpty():
        print(f"Dequeued: {queue.dequeue()}")

    print(f"\nIs Queue Empty after all dequeues?: {queue.isEmpty()}")
    print(f"Front Element now: {queue.peek()}")
    print(f"Dequeue when empty: {queue.dequeue()}")
