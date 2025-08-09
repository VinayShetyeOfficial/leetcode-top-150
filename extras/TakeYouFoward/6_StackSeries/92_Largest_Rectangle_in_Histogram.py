# Link: https://takeuforward.org/plus/dsa/problems/largest-rectangle-in-a-histogram

# Area of largest rectangle in Histogram

def largestRectangleArea(heights: list[int]) -> int:
    maxArea = 0
    stack = []  # This stack stores pairs of (index, height)

    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            index, height = stack.pop()
            maxArea = max(maxArea, height * (i - index))
            start = index
        stack.append((start, h))

    for i, h in stack:
        maxArea = max(maxArea, h * (len(heights) - i))

    return maxArea


# 🔽 Test Cases
if __name__ == '__main__':
    test_cases = [
        ([2, 1, 5, 6, 2, 3], 10),      # Classic example
        ([2, 4], 4),                   # Simple increasing
        ([2, 1, 2], 3),                # Valley shape
        ([6, 2, 5, 4, 5, 1, 6], 12),   # Zigzag heights
        ([1, 1, 1, 1], 4),             # All same height
        ([4, 3, 2, 1], 6),             # Decreasing bars
        ([1, 2, 3, 4, 5], 9),          # Increasing bars
        ([1], 1),                      # Single bar
        ([3, 5, 1, 7, 5, 9], 15),      # Custom case from your main code
    ]

    for i, (heights, expected) in enumerate(test_cases, 1):
        result = largestRectangleArea(heights)
        print(f'Test Case {i}: Input = {heights}')
        print(f'Expected: {expected}, Got: {result}')
        print('Pass ✅\n' if result == expected else 'Fail ❌\n')
        
