# Doubly Linked List

class Node:
    def __init__(self, data, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev  = current
            
    def printList(self):
        current = self.head
        
        # Forward Traversal
        print("Forward Traversal:")
        while current:
            print(current.data, end = ' -> ')
            if current.next:
                current = current.next
            else: break
        print(None)
        
         # Backward Traversal from the last node
        print("Backward Traversal:")
        while current:
            print(current.data, end = ' -> ')
            if current.prev:
                current = current.prev
            else:
                break
        print(None)
        
if __name__ == '__main__':
    ll = LinkedList()
    ll.insert(10)
    ll.insert(20)
    ll.insert(30)
    ll.insert(40)
    ll.insert(50)
    ll.printList()
            