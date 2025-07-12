# Link: https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/

# Decrypt String from Alphabet to Integer Mapping
class Solution(object):
    def freqAlphabets(self, s):
        charSet1 = {str(i): chr(96 + i) for i in range(1, 10)}
        # {'1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f', '7': 'g', '8': 'h', '9': 'i'}
        charSet2 = {str(i) + '#': chr(96 + i) for i in range(10, 27)}
        # {'10#': 'j', '11#': 'k', '12#': 'l', '13#': 'm', '14#': 'n', '15#': 'o', 
        # '16#': 'p', '17#': 'q', '18#': 'r', '19#': 's', '20#': 't', '21#': 'u', 
        # '22#': 'v', '23#': 'w', '24#': 'x', '25#': 'y', '26#': 'z'}

        i = 0
        res = ""
        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == '#':
                res += charSet2[s[i:i+3]]
                i += 3
            else:
                res += charSet1[s[i]]
                i += 1
                
        return res

# Driver code
if __name__ == '__main__':
    obj = Solution()
    s = "10#11#12"
    print(obj.freqAlphabets(s))  # Output: "jkab"
