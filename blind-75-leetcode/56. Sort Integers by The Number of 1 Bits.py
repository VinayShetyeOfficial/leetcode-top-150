# Links: https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/description/

# Sort Integers by The Number of 1 Bits
class Solution(object):
    def bitCount(n):
        count = 0
        while n:
            n &= (n - 1)
            count += 1
        return count

    # Sort using tuple: (bit count, original value)
    return sorted(arr, key = lambda x: (bitCount(x), x))

# OR 

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        
        return sorted(arr, key=lambda num: (num.bit_count(), num))

# =======================================================

# Alternate Solution

class Solution(object):
    def sortByBits(self, arr):
        def count_of_bits(num):
            binary = bin(num)
            count = binary.count('1')
            
            return (count, num)            
        
        arr.sort(key=count_of_bits)
        return arr
        
# Driver code
if __name__ == '__main__':
    obj = Solution()
    arr = [1024,512,256,128,64,32,16,8,4,2,1]
    print(obj.sortByBits(arr))

# =======================================================   

# Alternate Solution

class Solution(object):
    def sortByBits(self, arr):
        # Bubble Sort
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                curr_element = bin(arr[j]).count('1')
                next_element = bin(arr[j+1]).count('1')
                if curr_element > next_element:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                elif curr_element == next_element:
                    if arr[j] > arr[j+1]:
                        arr[j], arr[j+1] = arr[j+1], arr[j]
                    
        return arr
        
# Driver code
if __name__ == '__main__':
    obj = Solution()
    arr = [1024,512,256,128,64,32,16,8,4,2,1]
    print(obj.sortByBits(arr))
