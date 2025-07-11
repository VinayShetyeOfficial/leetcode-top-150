# Links: https://leetcode.com/problems/verifying-an-alien-dictionary/description/

# Verifying an Alien Dictionary
class Solution(object):
    def isAlienSorted(self, words, order):
        order_index = {char: i for i, char in enumerate(order)}
        
        def is_sorted(word1, word2):
            for c1, c2 in zip(word1, word2):
                if order_index[c1] < order_index[c2]:
                    return True
                elif order_index[c1] > order_index[c2]:
                    return False
            return len(word1) <= len(word2)
        
        for i in range(len(words) - 1):
            if not is_sorted(words[i], words[i + 1]):
                return False
        return True
        
# Driver code
if __name__ == '__main__':
    obj = Solution()
    
    words = ["hello","leetcode"]
    order = "hlabcdefgijkmnopqrstuvwxyz"
    print(obj.isAlienSorted(words, order))
    