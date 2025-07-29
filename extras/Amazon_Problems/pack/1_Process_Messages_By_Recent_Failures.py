# Process Messages by Recent Failures

def processMessages(messages):
    """
    Given a list of messages with '_' as day separators,
    return the messages reordered based on the rules:
    - Start from the most recent day
    - For each day, process messages in order
    - Stop at the first failure message
    """
    def isFailure(message):
        fail_messages = ['F', 'X']
        return message in fail_messages
    
    result = []
    groups = ''.join(messages).split('_')[::-1]
    
    for index, group in enumerate(groups):
        for message in group:
            if isFailure(message):
                result.append(message)
                break
            result.append(message)

        if index < len(groups) - 1:
            result.append('_')
            
    return result

# Example usage
if __name__ == '__main__':
    messages = ['A', 'B', 'C', '_', 'D', 'F', 'E', '_', 'X', 'Y', 'Z']
    result = processMessages(messages)
    print("Processed Messages:", result)
    # Output: Processed Messages: ['X', '_', 'D', 'F', '_', 'A', 'B', 'C']
