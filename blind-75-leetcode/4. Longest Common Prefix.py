# Link: https://leetcode.com/problems/longest-common-prefix/description/

# Longest Common Prefix
class Solution():
    def longestCommonPrefix(self, strs):
        temp = []
        # temp = ""   # Alternative if you want string output instead of list

        # Step 1: Find the string with minimum length
        min_len = min(strs, key=len)
        
        # Step 2: Iterate over characters of the smallest string
        for i in range(len(min_len)):
            res = [x[i] for x in strs]
            
            # Step 3: Check if all characters at this position are equal
            if len(set(res)) != 1:
                # Alternate checks:
                # if res.count(res[0]) != len(strs):
                # if any(x[i] != res[0] for x in strs):
                break
            
            temp += res[0]
        
        return len(temp)    # Returns length
        # return "".join(temp)   # ⭐ If you want actual string prefix

# ------------------------------
# Sub-step functions
# ------------------------------

# ⭐1. Find element with the minimum string length
def min_length(array):
    return min(array, key=len)


# ⭐2. Determine if all elements in array are equal
def all_equal(lst):
    return len(set(lst)) == 1
    # return all(x == lst[0] for x in lst)
    # return lst.count(lst[0]) == len(lst)


# ------------------------------
# Driver code
# ------------------------------
if __name__ == "__main__":
    obj = Solution()
    
    strs1 = ["flower", "flow", "flight"]
    strs2 = ["integration", "integer", "integral", "integrate", "intellect", "intelligent", "intelligible", "intend", "intensity", "intense"]
    strs3 = ["submarine", "submerge", "submit", "subway", "subsequent", "subscribe", "substitute", "subtle", "subdivision"]
    strs4 = ["spectacular", "spectrum", "speculate", "specimen", "specification", "specific", "species", "specter"]
    strs5 = ["automobile", "automatic", "automate", "automaton", "autonomous", "autonomy", "autopsy"]
    strs6 = ["transformation", "transmit", "transport", "transfusion", "translucent", "translate"]
    
    print("Longest Common Prefix Length:", obj.longestCommonPrefix(strs1))
    
    # Sub-step 1
    array1 = ["flower", "flow", "flight"]
    array2 = ["interstellar", "internet", "interval", "interview"]
    array3 = ["programming", "programmer", "program", "progress", "proton"]
    
    print("Min length string in array1:", min_length(array1))
    print("Min length string in array2:", min_length(array2))
    print("Min length string in array3:", min_length(array3))
    
    # Sub-step 2
    lst = [1, 1, 1, 1]
    print("All elements equal?:", all_equal(lst))


"""
===========================================
Time Complexity (TC):
- Finding min length string: O(n) 
- Iterating over characters: O(m * n), where
    n = number of strings, m = length of shortest string
- Overall: O(m * n)

Space Complexity (SC): O(1)
- Only a few extra variables used (temp, res, etc.)
- No extra space proportional to input size.
===========================================
"""
