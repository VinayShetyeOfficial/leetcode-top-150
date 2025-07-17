# Search an element in a Linked List

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    # INSERT NODE AT THE END
    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    # PRINT LINKED LIST
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print('None')

    # FIND LENGTH OF THE LIST
    def list_length(self):
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
        return length

    # CHECK IF VALUE EXISTS IN LIST
    def find_val(self, val):
        current = self.head
        while current:
            if current.data == val:
                return True
            current = current.next
        return False
