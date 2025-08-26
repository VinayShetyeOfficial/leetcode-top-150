# ============================================
# Integer to Binary & Binary to Integer
# ============================================

# Integer ➝ Binary Conversion
def int_to_bin(num: int) -> str:
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


# Binary ➝ Integer Conversion (Approach 1)
def bin_to_int(binary: str) -> int:
    res = 0
    binary = binary[::-1]  # reverse string for position mapping
    for i in range(len(binary)):
        if binary[i] == '1':
            res += 2 ** i
    return res


# Binary ➝ Integer Conversion (Approach 2)
def bin_to_int_alt(binary: str) -> int:
    res = 0
    for i in range(len(binary)):
        if binary[i] == "1":
            res += 2 ** (len(binary) - i - 1)
    return res


# Binary ➝ Integer Conversion (Approach 3: Validation + digits math)
def is_binary(num: int) -> bool:
    num_str = str(num)
    return all(digit in '01' for digit in num_str)

def bin_to_int_with_validation(binary: int) -> None:
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


# ============================================
# Driver Code
# ============================================
if __name__ == "__main__":
    # Integer ➝ Binary
    num = 12
    print(f"{num} to binary: {int_to_bin(num)}")  # 1100
    num = -53
    print(f"{num} to binary (32-bit two's complement): {int_to_bin(num)}")

    # Binary ➝ Integer
    print(bin_to_int("1101"))         # 13
    print(bin_to_int_alt("1011"))     # 11
    bin_to_int_with_validation(100)   # 4
    bin_to_int_with_validation(101)   # 5
    bin_to_int_with_validation(100141)  # Invalid


"""
============================================
Time Complexity (TC):
- int_to_bin: O(log n)  → because we divide num by 2 until it becomes 0
- bin_to_int (all versions): O(k), where k = length of binary string

Space Complexity (SC):
- int_to_bin: O(log n) for storing binary string
- bin_to_int: O(1) extra space
============================================
"""
