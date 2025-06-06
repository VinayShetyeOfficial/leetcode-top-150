# 68. Text Justification (Hard) 
# https://leetcode.com/problems/text-justification

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        """
        Fully justifies the given list of words to fit into lines of maxWidth.
        """
        res = []                   # Result list to hold each justified line
        current_line = []          # Words for the current line
        current_length = 0         # Total length of words (excluding spaces)

        i = 0
        while i < len(words):
            word = words[i]

            # Check if adding this word exceeds maxWidth (accounting for space between words)
            if current_length + len(current_line) + len(word) > maxWidth:
                total_spaces = maxWidth - current_length
                number_of_gaps = max(1, len(current_line) - 1)
                even_space = total_spaces // number_of_gaps
                extra_space = total_spaces % number_of_gaps

                # Distribute spaces
                for j in range(number_of_gaps):
                    current_line[j] += ' ' * even_space
                    if extra_space > 0:
                        current_line[j] += ' '
                        extra_space -= 1

                # Append the justified line
                res.append(''.join(current_line))
                current_line = []
                current_length = 0

            # Add current word to the line
            current_line.append(word)
            current_length += len(word)
            i += 1

        # Last line - left-justified
        last_line = ' '.join(current_line)
        res.append(last_line + ' ' * (maxWidth - len(last_line)))

        return res
    
"""
✅ Time Complexity: O(n * k)
👉 Where n = number of words, k = maxWidth

✅ Space Complexity: O(1) extra (excluding output)
👉 No significant extra memory used besides the result list.
"""
