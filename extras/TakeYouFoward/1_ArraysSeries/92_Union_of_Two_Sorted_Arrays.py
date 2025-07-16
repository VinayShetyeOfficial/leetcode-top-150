# Union of Two Sorted Arrays

def unionArray(nums1: list[int], nums2: list[int]) -> list[int]:
    return sorted(set(nums1) | set(nums2))

if __name__ == "__main__":
    nums1 = [3, 4, 6, 7, 9, 9]
    nums2 = [1, 5, 7, 8, 8]
    ans = unionArray(nums1, nums2)
    print("Union Result:", ans)

# ===================================================================

# Alternative approach:

# 🫴🏾 Dictionary avoids duplicates keys 🫳🏾
def unionArray(nums1: list[int], nums2: list[int]) -> list[int]:
    freq = {}
    for num in nums1 + nums2:
        freq[num] = True
        
    # Convert keys to list and sort using basic sort (if built-in sort is not allowed)
    keys = list(freq.keys())
    
    # Optional: if you want to sort manually, else use keys.sort()
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            if keys[i] > keys[j]:
                keys[i], keys[j] = keys[j], keys[i]

    return keys

if __name__ == "__main__":
    nums1 = [3, 4, 6, 7, 9, 9]
    nums2 = [1, 5, 7, 8, 8]
    ans = unionArray(nums1, nums2)
    print("Union Result:", ans)

# ===================================================================

# Without use of inbuilt methods
def unionArray(nums1: list[int], nums2: list[int]) -> list[int]:
    union = []
    
    # Add unique elements from nums1
    for num in nums1:
        if num not in union:
            union.append(num)
    
    # Add unique elements from nums2
    for num in nums2:
        if num not in union:
            union.append(num)
            
    # Sort manually (using bubble sort - n^2)
    n = len(union)
    for i in range(n):
        for j in range(n - i - 1):
            if union[j] > union[j + 1]:
                union[j], union[j + 1] = union[j + 1], union[j]
                
    return union
    

if __name__ == "__main__":
    nums1 = [3, 4, 6, 7, 9, 9]
    nums2 = [1, 5, 7, 8, 8]
    ans = unionArray(nums1, nums2)
    print("Union Result:", ans)
