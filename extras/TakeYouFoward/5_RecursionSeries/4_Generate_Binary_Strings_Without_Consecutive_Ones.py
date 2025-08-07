# Link: https://takeuforward.org/plus/dsa/problems/generate-binary-strings-without-consecutive-1s

# Generate Binary Strings Without Consecutive 1s

def generateBinaryStrings(n: int) -> list[str]:
    # Helper function to check for consecutive 1's
    def has_consecutive_ones(n: int) -> bool:
        return(n & (n >> 1)) != 0
    
    result = []
    for i in range(2**n):
        check_num  = bin(i)[2:].zfill(n)
        if not has_consecutive_ones(i):
            result.append(check_num)
            
    return result
    
if __name__ == '__main__':
    num = 3
    ans = generateBinaryStrings(num)
    print(f'Result: {ans}')
