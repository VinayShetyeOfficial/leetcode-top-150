# Link: https://leetcode.com/problems/plus-one/

# Plus One
class Solution(object):
    def plusOne(self, digits):
        if not digits:
            return None
        
        # Traverse the list from the last digit backwards
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:          # If current digit < 9, just increment and return
                digits[i] += 1
                return digits
            else:                      # If current digit = 9, turn it into 0 and continue loop
                digits[i] = 0
        
        # If all digits were 9, e.g., [9,9] -> [1,0,0]
        digits.insert(0, 1)   # Insert 1 at the beginning
        
        return digits

# Driver code
if __name__ == "__main__":
    obj = Solution()
    print(obj.plusOne([1, 2, 3]))   # Output: [1, 2, 4]
    print(obj.plusOne([4, 3, 2, 1]))  # Output: [4, 3, 2, 2]
    print(obj.plusOne([9, 9]))  # Output: [1, 0, 0]


"""
Time Complexity (TC): O(n) 
- We may traverse all digits once in the worst case (like [9,9,9,...]).
- Inserting at the beginning using `insert(0, 1)` is O(n) because all elements shift.
- So overall still O(n).

Space Complexity (SC): O(1) 
- We modify the digits list in place. No extra space apart from a few variables.
"""
