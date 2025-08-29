# Link: https://takeuforward.org/plus/dsa/problems/union-of-two-sorted-arrays

# Union of Two Sorted Arrays

def unionArray(nums1: list[int], nums2: list[int]) -> list[int]:
    return sorted(set(nums1) | set(nums2))

if __name__ == "__main__":
    nums1 = [3, 4, 6, 7, 9, 9]
    nums2 = [1, 5, 7, 8, 8]
    ans = unionArray(nums1, nums2)
    print("Union Result:", ans)

# Time Complexity (TC): O((N+M) log(N+M)) -> set creation O(N+M), sorting O((N+M) log(N+M))
# Space Complexity (SC): O(N+M) -> for set and result array


# ===================================================================

# Alternative approach using dictionary

def unionArray(nums1: list[int], nums2: list[int]) -> list[int]:
    freq = {}
    for num in nums1 + nums2:
        freq[num] = True
        
    keys = list(freq.keys())
    
    # Manual sorting (bubble sort)
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

# Time Complexity (TC): O((N+M)^2) -> due to bubble sort
# Space Complexity (SC): O(N+M) -> for dictionary keys


# ===================================================================

# Without using inbuilt methods

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
            
    # Manual bubble sort
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

# Time Complexity (TC): O((N+M)^2) -> due to checking duplicates + bubble sort
# Space Complexity (SC): O(N+M) -> for the union array
