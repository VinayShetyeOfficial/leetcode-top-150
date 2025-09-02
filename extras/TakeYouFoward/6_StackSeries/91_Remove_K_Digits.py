# Link: https://takeuforward.org/plus/dsa/problems/remove-k-digits

# Remove K Digits
# Given a string nums representing a non-negative integer, and an integer k, 
# find the smallest possible integer after removing k digits from num.

def removeKdigits(nums: str, k: int) -> str:
    if k == len(nums):
        return '0'

    stack = []

    for num in nums:
        # Remove digits from the stack if current num is smaller
        while stack and k > 0 and num < stack[-1]:
            stack.pop()
            k -= 1
        stack.append(num)

    # If k digits still remain, remove from end
    stack = stack[:len(stack) - k] if k else stack

    # Join and remove leading zeros
    result = ''.join(stack).lstrip('0')

    # Return '0' if result is empty
    return result if result else '0'


# ----------- Test Driver Code -----------
if __name__ == '__main__':
    test_cases = [
        ("1230456", 3),   # "0456" -> "45"
        ("1432219", 3),   # "1219"
        ("10200", 1),     # "200"
        ("10", 2),        # "0"
        ("112", 1),       # "11"
        ("10001", 4),     # "0"
        ("9", 1),         # "0"
        ("1111111", 3),   # "1111"
        ("7654321", 3),   # "4321"
    ]

    for nums, k in test_cases:
        ans = removeKdigits(nums, k)
        print(f'Input: nums="{nums}", k={k} → Result: {ans}')


"""
Time Complexity: O(n), where n is the length of the input string `nums`. 
                 Each digit is pushed and popped at most once.
Space Complexity: O(n), for the stack used to store digits.
"""
