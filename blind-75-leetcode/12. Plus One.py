# Link: https://leetcode.com/problems/plus-one/

# Plus One
class Solution(object):
    def plusOne(self, digits):
        if not digits:
            return None
        
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        
        digits.insert(0, 1)
        # x = [1]
        # x.extend(digits)  
        
        return digits  
        # return x 

# Driver code
if __name__ == "__main__":
    # Example usage:
    obj = Solution()
    print(obj.plusOne([1, 2, 3]))  
    print(obj.plusOne([4, 3, 2, 1]))  
    print(obj.plusOne([9, 9]))  


# Sub-steps Requirements
# ----------------------

# ⭐1. Program to => `Perform append at the beginning of the List`:
# Link: https://www.geeksforgeeks.org/python-perform-append-at-beginning-of-list/