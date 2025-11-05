# https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/time-slot-task-pairing

def findTaskPairForSlot(taskDurations, slotLength):
    # Write your code here
    numMap = {}
    
    for index, number in enumerate(taskDurations):
        complement = slotLength - number
        if complement in numMap:
            return [numMap[complement], index]
        
        numMap[number] = index

    return [-1, -1]

