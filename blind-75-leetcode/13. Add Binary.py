# Link: https://leetcode.com/problems/add-binary/description/

#  Add Binary
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ''
        carry = 0

        # Reverse the two strings for easier left-to-right processing
        a, b = a[::-1], b[::-1]

        # Loop through the longer of the two strings
        for i in range(max(len(a), len(b))):    
            digitA = int(a[i]) if i < len(a) else 0
            digitB = int(b[i]) if i < len(b) else 0

            total = digitA + digitB + carry
            result = str(total % 2) + result # Add the current binary digit
            carry = (total // 2) # update the carry

        if carry:
            result = '1' + result

        return result 

# ============================================================================

# ⭐ From Scratch - Executable Code ⭐

#  Add Binary
class Solution(object):
    def addBinary(self, a, b):
        result = (self.bin_to_int(int(a)) + self.bin_to_int(int(b)))
        
        return self.int_to_bin(result)
    
    def bin_to_int(self, binary):
     
        integer, i = 0, 0
        while binary > 0:
            dec = binary % 10
            integer = integer + dec * pow(2, i)
            binary = binary//10
            i += 1
        
        return integer
     
     
    def int_to_bin(self, num):
    
        if num == 0:
            return "0"
        
        binary = ""
        while num > 0:
            remainder = num % 2
            binary = str(remainder) + binary
            num = num // 2
        
        return binary
 
# Driver code
if __name__ == '__main__':
    obj = Solution()
    a = "1010"
    b = "1011"
    print(obj.addBinary(a, b))
    


