# Link: https://leetcode.com/problems/single-number/

# ============================================
# Approach 1: Using HashMap / Dictionary
# ============================================
class SingleNumberHashMap(object):
    def singleNumber(self, nums):
        hashmap = {x: nums.count(x) for x in nums}
        
        # Finding the key with the minimum value (appears once)
        min_val = min(hashmap, key=hashmap.get)
        return min_val

"""
Time Complexity (TC): O(n^2)
- nums.count(x) is O(n), done for n elements.

Space Complexity (SC): O(n)
- HashMap stores counts for each unique number.
"""

# ============================================
# Approach 2: Brute Force (Check each element)
# ============================================
class SingleNumberBruteForce(object):
    def singleNumber(self, nums):
        for i, num in enumerate(nums):
            if num not in nums[:i] and num not in nums[i+1:]:
                return num
        return None

"""
Time Complexity (TC): O(n^2)
- For each element, we scan the rest of the list.

Space Complexity (SC): O(1)
- No extra space used.
"""

# ============================================
# Approach 3: XOR Method (Optimal)
# ============================================
class SingleNumberXOR(object):
    def singleNumber(self, nums):
        answer = 0
        for n in nums:
            answer ^= n  # XOR operation cancels duplicates
        return answer

"""
Time Complexity (TC): O(n)
- Single pass through the list.

Space Complexity (SC): O(1)
- Only one variable used.
"""

# ============================================
# Driver Code
# ============================================
if __name__ == '__main__':
    nums = [2, 2, 1, 4, 3, 5, 4, 3, 5]

    # HashMap Solution
    obj1 = SingleNumberHashMap()
    print("HashMap Solution:", obj1.singleNumber(nums))  # Output: 1

    # Brute Force Solution
    obj2 = SingleNumberBruteForce()
    print("Brute Force Solution:", obj2.singleNumber(nums))  # Output: 1

    # XOR Solution
    obj3 = SingleNumberXOR()
    print("XOR Solution:", obj3.singleNumber(nums))  # Output: 1
