# https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/first-occurrence-in-event-code-log/

def findFirstOccurrence(nums, target):
    low, high = 0, len(nums) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            result = mid           # Record potential answer
            high = mid - 1         # Continue searching left side
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return result
