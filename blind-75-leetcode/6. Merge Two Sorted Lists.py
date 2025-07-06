# Link: https://leetcode.com/problems/merge-two-sorted-lists/description/

# Merge Two Sorted Lists
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if None in [list1, list2]:
            return list1 or list2
        
        List = []
        temp1 = list1
        temp2 = list2
        
        while temp1 or temp2:
            if temp1:
                List.append(temp1)
                temp1 = temp1.next
                
            if temp2:
                List.append(temp2)
                temp2 = temp2.next
        
        List = self.bubbleSort(List)
        
        for i in range(len(List) - 1):
            List[i].next = List[i + 1]
        List[-1].next = None  
        
        return List[0]
        
    def bubbleSort(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j].val > arr[j + 1].val:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr
    
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

# Driver code
if __name__ == "__main__":
    obj = Solution()
    
    list1 = createLinkedList([1, 2, 4])
    list2 = createLinkedList([1, 3, 4])
    
    mergedList = obj.mergeTwoLists(list1, list2)
    
    printLinkedList(mergedList)



# Sub-steps Requirements
# ----------------------

# ⭐1. Program to => `perform BubbleSort`:
def bubbleSort(arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1],arr[j]
    return arr

# Driver code
if __name__ == "__main__":
    arr = [6,4,7,1,2,9,5,0,8,3] 
    print("Sorted Array: ", bubbleSort(arr))
