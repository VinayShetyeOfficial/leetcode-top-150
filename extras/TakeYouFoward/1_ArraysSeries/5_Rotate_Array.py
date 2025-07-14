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
