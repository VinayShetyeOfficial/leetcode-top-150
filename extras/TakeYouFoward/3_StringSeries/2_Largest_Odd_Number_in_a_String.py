# Link: https://takeuforward.org/plus/dsa/problems/largest-odd-number-in-a-string

# Largest Odd Number in a String

def largeOddNum(s: str) -> str:
    # Traverse the string from right to left
    for i in range(len(s) - 1, -1, -1):
        if int(s[i]) % 2 == 1:  # Check if the digit is odd
            return str(int(s[:i + 1]))  # Convert to int to remove leading zeros
    return ""  # No odd digit found
     
if __name__ == '__main__':
    s = "0032579224466"
    ans = largeOddNum(s)
    print(f'Largest Odd Number Possible: {ans}')

"""
Time Complexity (TC): O(N) -> single pass from right to left
Space Complexity (SC): O(1) -> only using indices and slicing, extra space negligible
"""
