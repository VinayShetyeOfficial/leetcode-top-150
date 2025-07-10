# Link: https://leetcode.com/problems/reverse-words-in-a-string-iii/

# Reverse Words in a String III
class Solution(object):
    def reverseWords(self, s):
        res = []
        
        res += s.split(" ")
        
        return " ".join([w[::-1] for w in res])
    
# Driver code
if __name__ == '__main__':
    obj = Solution()
    s = "Let's take LeetCode contest"
    print(obj.reverseWords(s))


