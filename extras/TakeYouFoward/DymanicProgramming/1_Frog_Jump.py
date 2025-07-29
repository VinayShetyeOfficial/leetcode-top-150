# Frog Jump
# https://takeuforward.org/plus/dsa/problems/frog-jump

def frogJump(heights):
    if not heights:
        return 0

    n = len(heights)
    prev = 0        # dp[i-1]
    prev2 = 0       # dp[i-2]

    for i in range(1, n):
        jump_one = prev + abs(heights[i] - heights[i-1])
        jump_two = float('inf')
        if i > 1:
            jump_two = prev2 + abs(heights[i] - heights[i-2])

        curr = min(jump_one, jump_two)
        prev2 = prev
        prev = curr

    return prev


if __name__ == '__main__':
    test_cases = [
        ([2, 1, 3, 5, 4], 2),
        ([7, 5, 1, 2, 6], 9),
        ([10], 0),
        ([10, 20], 10),
        ([30, 10, 60, 10, 60, 50], 40),
        ([1, 2, 3, 4, 5, 6], 5),
        ([6, 5, 4, 3, 2, 1], 5),
        ([1, 100, 1, 1, 100, 1], 0),  
        ([1, 3, 2, 4, 6, 2, 1], 6),  
        ([], 0),
    ]
    for i, (heights, expected) in enumerate(test_cases):
        result = frogJump(heights)
        print(f'Test Case {i+1}: heights = {heights}')
        print(f'Expected: {expected}, Got: {result}')
        print(f'✅ Pass\n' if result == expected else f'❌ Fail\n')
