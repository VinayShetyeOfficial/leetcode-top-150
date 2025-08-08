# Link: https://takeuforward.org/plus/dsa/problems/trapping-rainwater

# Trapping Rain Water

def trappingRainWater(height: list[int]) -> int:
    if not height: return 0

    left, right = 0, len(height) - 1
    max_left = height[left]
    max_right = height[right]
    total_water = 0

    while left < right:
        if max_left < max_right:
            left += 1
            max_left = max(max_left, height[left])
            total_water += max_left - height[left]
        else:
            right -= 1
            max_right = max(max_right, height[right])
            total_water += max_right - height[right]
    return total_water

# ----------- Test Driver Code -----------
if __name__ == '__main__':
    heights1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    heights2 = [4, 2, 0, 3, 2, 5]
    heights3 = [2, 0, 2]
    heights4 = [3, 0, 0, 2, 0, 4]
    heights5 = [1, 0, 1]


    print(f'Total Rain Water Units (1): {trappingRainWater(heights1)}')   # Expected: 6
    print(f'Total Rain Water Units (2): {trappingRainWater(heights2)}')   # Expected: 9
    print(f'Total Rain Water Units (3): {trappingRainWater(heights3)}')   # Expected: 2
    print(f'Total Rain Water Units (4): {trappingRainWater(heights4)}')   # Expected: 10
    print(f'Total Rain Water Units (5): {trappingRainWater(heights5)}')   # Expected: 1

