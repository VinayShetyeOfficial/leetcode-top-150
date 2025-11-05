# https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/remove-elements-within-k-distance/

def debounceTimestamps(timestamps, K):
    # Write your code here
    # If array is empty, nothing to keep
    if not timestamps:
        return 0
    
    # slow pointer: position of last kept element
    slow = 0
    
    # fast pointer: scans the array
    for fast in range(1, len(timestamps)):
        if timestamps[fast] - timestamps[slow] >= K:
            slow += 1
            timestamps[slow] = timestamps[fast]
    
    # New valid length is slow + 1
    return slow + 1

