# Link: https://takeuforward.org/plus/dsa/problems/generate-binary-strings-without-consecutive-1s

def generateBinaryStrings(n: int) -> list[str]:
    """
    Generate all binary strings of length n without consecutive 1s
    """

    def has_consecutive_ones(num: int) -> bool:
        """
        Check if binary representation of num has consecutive 1s
        """
        return (num & (num >> 1)) != 0

    result = []
    for i in range(2**n):
        binary_str = bin(i)[2:].zfill(n)
        if not has_consecutive_ones(i):
            result.append(binary_str)

    return result


if __name__ == '__main__':
    num = 3
    ans = generateBinaryStrings(num)
    print(f'Result: {ans}')  # Output: ['000', '001', '010', '100', '101']


"""
Time Complexity (TC): O(n * 2^n)
    -> We iterate over all 2^n numbers, and for each number we check for consecutive 1s in O(n) time.
Space Complexity (SC): O(n * 2^n)
    -> Storing all valid binary strings, each of length n.
"""
