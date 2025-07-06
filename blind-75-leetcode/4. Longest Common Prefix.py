# Link: https://leetcode.com/problems/longest-common-prefix/description/

# Longest Common Prefix
class Solution():
    def longestCommonPrefix(self, strs):
        temp = []
        # temp = ""         # Sample - Output Req: "fl"
        
        min_len = min(strs, key=len)
        
        for i in range(len(min_len)):
            res = [x[i] for x in strs]
            
            if len(set(res)) != 1:
            # if res.count(res[0]) != len(strs):  ⭐  # (different expression)
            # if any(x[i] != res[0] for x in strs):    # (different expression)
                break
            
            temp += res[0]
            
        return len(temp)
        # return temp

if __name__ == "__main__":
    obj = Solution()
    strs = ["flower","flow","flight"]
    # strs = ["integration", "integer", "integral", "integrate", "intellect", "intelligent", "intelligible", "intend", "intensity", "intense"]
    # strs = ["submarine", "submerge", "submit", "subway", "subsequent", "subscribe", "substitute", "subtle", "subdivision"]
    # strs = ["spectacular", "spectrum", "speculate", "specimen", "specification", "specific", "species", "specter"]
    # strs = ["automobile", "automatic", "automate", "automaton", "autonomous", "autonomy", "autopsy"]
    # strs = ["transformation", "transmit", "transport", "transfusion", "translucent", "translate"]
    print(obj.longestCommonPrefix(strs))
    



# Sub-steps Requirements
# ----------------------

# ⭐1. Program to find the => `element with the minimum string length`:
def min_length(array):
    return min(array, key=len)

print(min_length(array1))
print(min_length(array2))
print(min_length(array3))

array1 = ["flower", "flow", "flight"]
array2 = ["interstellar", "internet", "interval", "interview"]
array3 = ["programming", "programmer", "program", "progress", "proton"]


# ⭐2. Program to => `determine if all elements in array are equal``:
def all_equal(lst):
    return len(set(lst)) == 1
    # return all(x == lst[0] for x in lst)
    # return lst.count(lst[0]) == len(lst)

if __name__ == "__main__":
    lst = [1,1,1,1]
    print(all_equal(lst))