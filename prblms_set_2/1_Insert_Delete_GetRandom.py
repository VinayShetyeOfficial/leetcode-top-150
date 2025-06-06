# 380. Insert Delete GetRandom O(1) (Medium) - Done
# https://leetcode.com/problems/insert-delete-getrandom-o1

class RandomizedSet:
    def __init__(self):
        # Dictionary to map values to their index in the list
        self.value_to_index = {}

        # List to store current values
        self.values = []

    def insert(self, val: int) -> bool:
        """
        Inserts val if not already present.
        Returns True if inserted, False if it already exists.
        """

        if val in self.value_to_index:
            return False

        # Store the value and its index
        self.value_to_index[val] = len(self.values)
        self.values.append(val)

        return True

    def remove(self, val: int) -> bool:
        """
        Removes val if present.
        Returns True if removed, False if not present.
        """

        if val not in self.value_to_index:
            return False

        # Index of element to remove
        index_to_remove = self.value_to_index[val]

        # Get the last element
        last_value = self.values[-1]

        # Swap the last value with the value to remove
        self.values[index_to_remove] = last_value
        self.value_to_index[last_value] = index_to_remove

        # Remove last element
        self.values.pop()
        del self.value_to_index[val]

        return True

    def getRandom(self) -> int:
        """
        Returns a random element from the set.
        """

        return random.choice(self.values)


"""
✅ insert(val):     O(1)
✅ remove(val):     O(1)
✅ getRandom():     O(1)
✅ Space:           O(n), where n is the number of elements in the set
"""

# Simple Easy to understand (Same Solution, easy variables):
class RandomizedSet:

    def __init__(self):
        self.numMap = {}
        self.numList = []

    def insert(self, val: int) -> bool:
        res = val not in self.numMap
        
        if res:
            self.numMap[val] = len(self.numList)
            self.numList.append(val)
        
        return res
        
    def remove(self, val: int) -> bool:
        res = val in self.numMap

        if res:
            idx = self.numMap[val]
            lastVal = self.numList[-1]
            self.numList[idx] = lastVal
            self.numList.pop()
            self.numMap[lastVal] = idx
            del self.numMap[val]
        
        return res

    def getRandom(self) -> int:
        return random.choice(self.numList)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()