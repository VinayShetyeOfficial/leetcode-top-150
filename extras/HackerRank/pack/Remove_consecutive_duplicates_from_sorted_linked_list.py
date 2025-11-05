# https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/remove-consecutive-duplicates-sorted-list/

def deleteDuplicates(head):
    current = head

    while current and current.next:
        if current.data == current.next.data:
            # Skip duplicate node
            current.next = current.next.next
        else:
            # Move to next unique node
            current = current.next

    return head