# Link: https://leetcode.com/problems/add-binary/description/

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
    


