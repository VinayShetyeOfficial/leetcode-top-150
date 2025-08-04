# Link: https://takeuforward.org/plus/dsa/problems/left-rotate-array-by-one

# Rotate Array

def rotateArray(nums: list[int]) -> list[int]:
    n = len(nums)
    res = [0] * n
    for i in range(1, len(nums)):
        res[i - 1] = nums[i]
    
    res[n - 1] = arr[0]
    return res
    
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print(f'Rotated Array: {rotateArray(arr)}')

# Rotated Array: [2, 3, 4, 5, 1]

# =====================================================

def rotateArray(nums: list[int], k: int) -> list[int]:
    n = len(nums)
    res = [0] * n
    
    for i in range(n):
        ⭐new_index = (i + k) % n     # Rotate to right / clock-wise
        ⭐new_index = (i - k + n) % n # Rotate to left / anti-clock-wise
        res[new_index] = nums[i]
    
    return res
    
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print(f'Rotated Array: {rotateArray(arr, 3)}')
    
# Rotated Array: [3, 4, 5, 1, 2]              - Right Rotation

'''
🔄 Why do we use "+n" in (i - k + n) % n during left rotation?

When rotating an array to the left, calculating new positions like (i - k) can sometimes go negative.
For example:
    n = 6
    i = 1, 
    k = 3 → (1 - 3) % 6 = -2 % 6
    
    divident = divisor * quotient + remainder
    -2 = 6 * (-1) + remainder
    +6 - 2 = remainder
    remainder = 4
    
If you directly do -2 % n, Python handles it nicely and gives a positive index.
But in other languages like C, C++, or Java, -2 % n gives a negative result, which causes index errors.

✅ So, adding `+n` makes it safe and always gives a valid non-negative index:
    (i - k + n) % n

This trick ensures your rotation logic works cleanly and consistently across different languages.

📌 Summary:
- 👉 Right Rotation (clockwise):     (i + k) % n
- 👉 Left Rotation (anti-clockwise): (i - k + n) % n
'''