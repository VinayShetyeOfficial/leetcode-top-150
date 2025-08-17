# Link: https://leetcode.com/problems/merge-two-sorted-lists/description/

# ==============================================
# ListNode Class
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ==============================================
# Method 1: Efficient Merge using pointers (LeetCode style)
class SolutionEfficient:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()   # ✅ should create an object, not just reference
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        # Attach the remaining part
        tail.next = list1 if list1 else list2

        return dummy.next


# ==============================================
# Method 2: Using BubbleSort (less efficient)
class SolutionBubbleSort:
    def mergeTwoLists(self, list1, list2):
        if None in [list1, list2]:
            return list1 or list2
        
        nodes = []
        temp1, temp2 = list1, list2

        while temp1 or temp2:
            if temp1:
                nodes.append(temp1)
                temp1 = temp1.next
            if temp2:
                nodes.append(temp2)
                temp2 = temp2.next

        # Sort nodes based on value
        nodes = self.bubbleSort(nodes)

        # Reconnect nodes
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        nodes[-1].next = None

        return nodes[0]
    
    def bubbleSort(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j].val > arr[j + 1].val:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr


# ==============================================
# Helper Functions
def createLinkedList(vals):
    if not vals:
        return None
    head = ListNode(vals[0])
    current = head
    for val in vals[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def printLinkedList(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")


# ==============================================
# Sub-step Program: Bubble Sort (for array)
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# ==============================================
# Driver code
if __name__ == "__main__":
    # Test Linked List Merge
    list1 = createLinkedList([1, 2, 4])
    list2 = createLinkedList([1, 3, 4])

    print("Efficient Merge Result:")
    obj1 = SolutionEfficient()
    mergedList1 = obj1.mergeTwoLists(list1, list2)
    printLinkedList(mergedList1)

    list1 = createLinkedList([1, 2, 4])
    list2 = createLinkedList([1, 3, 4])

    print("BubbleSort Merge Result:")
    obj2 = SolutionBubbleSort()
    mergedList2 = obj2.mergeTwoLists(list1, list2)
    printLinkedList(mergedList2)

    # Test Sub-step Bubble Sort
    arr = [6, 4, 7, 1, 2, 9, 5, 0, 8, 3]
    print("Sorted Array:", bubbleSort(arr))


"""
===========================================
Time Complexity (TC):
- Efficient Merge: O(n + m), where n and m are lengths of the lists.
- BubbleSort Merge: O((n + m)²) due to nested loops in bubble sort.

Space Complexity (SC):
- Efficient Merge: O(1), just pointers used.
- BubbleSort Merge: O(n + m), extra array to store nodes.
===========================================
"""
