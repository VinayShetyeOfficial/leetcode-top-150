# ============================================
# Sort Integers by The Number of 1 Bits - LeetCode
# ============================================

from typing import List

# Optimized Approach using built-in bit_count()
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # Sort by tuple (number of 1s, original value)
        return sorted(arr, key=lambda num: (num.bit_count(), num))

# Alternate Approach using custom bit counting
class SolutionAlt(object):
    def sortByBits(self, arr):
        def count_of_bits(num):
            return (bin(num).count('1'), num)  # tuple: (bit count, original number)
        
        arr.sort(key=count_of_bits)
        return arr

# Brute-force Approach using Bubble Sort
class SolutionBF(object):
    def sortByBits(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                curr_bits = bin(arr[j]).count('1')
                next_bits = bin(arr[j+1]).count('1')
                
                # Swap if current has more 1s
                if curr_bits > next_bits:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                # If equal bits, sort by value
                elif curr_bits == next_bits and arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

# ============================================
# Driver Code
# ============================================
if __name__ == '__main__':
    arr = [1024,512,256,128,64,32,16,8,4,2,1]
    
    obj = Solution()
    print(obj.sortByBits(arr))  # Optimized
    
    obj_alt = SolutionAlt()
    print(obj_alt.sortByBits(arr))  # Alternate
    
    obj_bf = SolutionBF()
    print(obj_bf.sortByBits(arr))  # Brute-force

"""
Time Complexity (TC):
- Optimized & Alternate: O(n log n) for sorting, O(n * k) if custom bit counting used, where k = number of bits
- Brute-force Bubble Sort: O(n^2 * k)

Space Complexity (SC):
- Optimized & Alternate: O(n) for sorted array (or O(1) in-place for sort)
- Brute-force: O(1)
"""
