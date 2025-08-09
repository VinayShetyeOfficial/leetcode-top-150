# Integer to Binary 
--------------------

def int_to_bin(num):
    
    if num == 0:
        return '0'
    
    if num < 0:
        num = (1 << 32) + num  # two's complement for 32-bit
    
    binary = ''
    
    while num:
        rem = num % 2
        binary = str(rem) + binary
        num //= 2
        
    return binary

# Driver code
if __name__ == "__main__":
    num = 12
    res = int_to_bin(num)
    print("{} to binary: {}".format(num, res))


Explaination:
-------------
# Step-by-step for num = 12:
# 12 % 2 = 0 → binary = '0'        → 12 // 2 = 6
# 6 % 2  = 0 → binary = '00'       → 6 // 2 = 3
# 3 % 2  = 1 → binary = '100'      → 3 // 2 = 1
# 1 % 2  = 1 → binary = '1100'     → 1 // 2 = 0 (loop ends)


'''
(1 << 32) means 1 shifted left by 32 bits.

In binary, 1 is ...0001.

Shifting left by 32 bits adds 32 zeros to the right.

So (1 << 32) equals 2^32, which is 4294967296.

Why is it used here?

When you do:

python
Copy
Edit
num = (1 << 32) + num
and num is negative, you’re converting num into its 32-bit two’s complement unsigned representation.

For example, if num = -53:

(1 << 32) = 4294967296

4294967296 + (-53) = 4294967243

This number is how -53 is stored as a 32-bit unsigned integer in two’s complement form.
'''
=====================================================================================================

# ⭐[1] Binary to Integer
--------------------------

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


*********************************

# [2] Binary to Integer
-----------------------

def is_binary(num):
    num_str = str(num)
    return all(digit in '01' for digit in num_str)

def bin_to_int(binary):
    if not is_binary(binary):
        print("Input number not in binary format!")
        return

    binary = int(binary)
    result, power = 0, 0

    while binary:
        result += (binary % 10) * (2 ** power)
        binary //= 10
        power += 1

    print(result)

# Driver code
if __name__ == '__main__':
    bin_to_int(100)
    bin_to_int(101)
    bin_to_int(100141)




