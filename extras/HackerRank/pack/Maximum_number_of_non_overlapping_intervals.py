# https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/maximum-non-overlapping-interval

def maximizeNonOverlappingMeetings(meetings):
    if not meetings:
        return 0
    
    # Step 1: Sort by end time
    meetings.sort(key=lambda x: x[1])
    
    # Step 2: Greedily select meetings
    count = 1  # first meeting always selected
    last_end = meetings[0][1]
    
    for start, end in meetings[1:]:
        if start >= last_end:
            count += 1
            last_end = end
    
    return count