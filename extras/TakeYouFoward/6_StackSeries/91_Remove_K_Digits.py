# Remove K Digits

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


if __name__ == '__main__':
    test_cases = [
        ("1230456", 3),
        ("1432219", 3),
        ("10200", 1),
        ("10", 2),
        ("112", 1),
        ("10001", 4),
        ("9", 1),
        ("1111111", 3),
        ("7654321", 3),
    ]

    for nums, k in test_cases:
        ans = removeKdigits(nums, k)
        print(f'Input: nums="{nums}", k={k} → Result: {ans}')
