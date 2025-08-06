# Link: https://takeuforward.org/plus/dsa/problems/largest-odd-number-in-a-string

# Largest Odd Number in a String

def largeOddNum(s: str) -> str:
    for i in range(len(s) -1, -1, -1):
        if int(s[i]) % 2 == 1:
            return str(int(s[:i + 1]))  # int(ans) to remove prefixed zeros if any
    return ""
     
if __name__ == '__main__':
    s = "0032579224466"
    ans = largeOddNum(s)
    print(f'Lagest Odd Number Posssible: {ans}')