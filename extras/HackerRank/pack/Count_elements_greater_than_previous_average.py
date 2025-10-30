# https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/count-elements-greater-than-previous-average

def countResponseTimeRegressions(responseTimes):
    # Write your code here
    count = 0
    total = 0
    
    for index in range(1, len(responseTimes)):
        
        total += responseTimes[index - 1]
        if responseTimes[index] > total / index:
            count += 1 
            
    return count