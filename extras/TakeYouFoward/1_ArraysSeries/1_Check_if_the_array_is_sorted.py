# To check if number list is sorted or not [Ascending or Descending Order]

# For Ascending:
def isSortedAscending(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True

# For Descending:
def isSortedDescending(arr):
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            return False
    return True

# For General:
def isSorted(arr):
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1)) or \
           all(arr[i] >= arr[i+1] for i in range(len(arr)-1))



'''
Special Case:
-------------
You’re testing it with a single-element list: [1].

Step-by-step:
len(arr) = 1

range(len(arr) - 1) = range(0)
→ This means the loop has zero iterations.

So both generators inside all():

all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1))

...are working over an empty sequence.



Q) Why does all([]) return True?
--------------------------------
This is a very important point.

all([]) returns True by definition (this is called vacuous truth in logic).

It means: "There is no element that makes the condition false."
Since there are no elements at all, none violate the condition.

So what happens here?
all(...) for both ascending and descending returns True (because they're checking an empty list of comparisons).

So the function returns True. 
'''