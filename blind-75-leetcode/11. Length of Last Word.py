# Link: https://leetcode.com/problems/length-of-last-word/description/

# Length of Last Word
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.strip().split(" ")[-1])
    

# ⭐ Without using inbuilt methods ⭐
class Solution(object):
    def lengthOfLastWord(self, s):
        length = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] != " ":
                length += 1
            elif length > 0:
                break
        return length

# Driver code                 
if __name__ == "__main__":
    obj = Solution()
    s = "luffy is still joyboy"
    # s = "   fly me   to   the moon  "
    # s = "Hello World"
    print(obj.lengthOfLastWord(s))
        