# Using the | Operator
set1 = {1, 2, 3}
set2 = {3, 4, 5}

result = set1 | set2
print(result)  # Output: {1, 2, 3, 4, 5}

# ----------------------

# Using the union Method
set1 = {1, 2, 3}
set2 = {3, 4, 5}

result = set1.union(set2)
print(result)  # Output: {1, 2, 3, 4, 5}

# ----------------------

# In-Place Union with update Method
# If you want to modify one of the sets in-place to include the elements from the other set, you can use the update method:
set1 = {1, 2, 3}
set2 = {3, 4, 5}

set1.update(set2)
print(set1)  # Output: {1, 2, 3, 4, 5}