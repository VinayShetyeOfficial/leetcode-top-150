# Links: https://leetcode.com/problems/reverse-bits/submissions/1298329410/

# Reverse Bits
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        k=format(n, '032b')
        rev=k[::-1]
        
        return int(rev,2)
        # return int(str('{0:032b}'.format(n))[::-1], 2)  # Optional

# Driver code
if __name__ == '__main__':
    obj = Solution()
    print(obj.reverseBits(00000010100101000001111010011100))