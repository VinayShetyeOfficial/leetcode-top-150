# 6. Zigzag Conversion (Medium)
# https://leetcode.com/problems/zigzag-conversion

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        Converts the input string s into a zigzag pattern with numRows,
        then reads it row by row to form the output string.
        """

        # Edge case: no zigzag possible
        if numRows == 1 or numRows >= len(s):
            return s

        # Initialize rows
        rows = [''] * numRows
        current_row = 0
        going_down = False

        # Place characters in appropriate rows
        for char in s:
            rows[current_row] += char
            # Change direction at top or bottom
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            # Move up or down
            current_row += 1 if going_down else -1

        # Join all rows to form the final result
        return ''.join(rows)
    
    
"""
✅ Time Complexity: O(n) – Each character is visited once.
✅ Space Complexity: O(n) – We store characters in rows.
"""
