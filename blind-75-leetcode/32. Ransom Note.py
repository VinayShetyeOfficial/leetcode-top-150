# Link: https://leetcode.com/problems/ransom-note/description/

# Ransom Note
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        for c in set(ransomNote):
            if ransomNote.count(c) > magazine.count(c):
                return False
        
        return True
    
# Driver code
if __name__ == '__main__':
    obj = Solution()
    ransomNote = "aa"
    magazine = "aab"
    print(obj.canConstruct(ransomNote, magazine))
