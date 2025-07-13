# Integer to Binary 
def int_to_bin(num):

    if num == 0:
        return "0"
    
    binary = ""
    
    while num > 0:
        remainder = num % 2
        binary = str(remainder) + binary
        num = num // 2
    
    return binary

# Driver code
if __name__ == "__main__":
    num = 8
    res = int_to_bin(num)
    print("{} to binary: {}".format(num, res))



# ⭐[1] Binary to Integer
def bin_to_int(num):
    
    res = 0
    num = num[::-1]
    
    for i in range(len(num)):
        res += 2**(i) if num[i] == '1' else 0
    
    
    return res

# ============== OR ==============

def bin_to_int(num):
    
    res = 0
    for i in range(len(num)):
        res += 2**(len(num)-i-1) if num[i] == "1" else 0
    
    return res

if __name__ == '__main__':
    print(bin_to_int("1101"))

# [2] Binary to Integer
def bin_to_int(binary):
 
    integer, i = 0, 0
    while binary > 0:
        dec = binary % 10
        integer = integer + dec * pow(2, i)
        binary = binary//10
        i += 1
    print(integer)

# Driver code
if __name__ == '__main__':
    bin_to_int(100)
    bin_to_int(101)
    bin_to_int(1001)



