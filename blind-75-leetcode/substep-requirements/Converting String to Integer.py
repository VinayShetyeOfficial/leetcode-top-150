# 1. Using int() Function
# The most common and straightforward method to convert a string to an integer is by using the built-in int() function.

s = "123"
num = int(s)
print(num)  # Output: 123

# /*================================================================

# 2. Using float() Followed by int()
# If the string might represent a float, you can first convert it to a float and then to an integer.
s = "123.45"
num = int(float(s))
print(num)  # Output: 123

# /*================================================================

# 3. Using eval() Function
# Although generally not recommended due to security reasons, eval() can also be used to convert a string to an integer.
s = "123"
num = eval(s)
print(num)  # Output: 123

# /*================================================================

# 4. Using ast.literal_eval()
# The literal_eval() method from the ast module is safer than eval() and can be used for this purpose.
import ast

s = "123"
num = ast.literal_eval(s)
print(num)  # Output: 123

# /*================================================================

# 5. Using Custom Function with ASCII Values
# You can write a custom function to convert a string to an integer by processing each character.
def str_to_int(s):
    result = 0
    for char in s:
        result = result * 10 + (ord(char) - ord('0'))
    return result

s = "123"
num = str_to_int(s)
print(num)  # Output: 123

# /*================================================================

# 6. Using List Comprehension and join()
# This method involves using list comprehension to filter numeric characters, then joining them back into a string and converting to an integer.
s = "123abc"
num = int(''.join([char for char in s if char.isdigit()]))
print(num)  # Output: 123

# /*================================================================

# 7. Using Regular Expressions
# Regular expressions can be used to extract the numeric part of a string and then convert it.
import re

s = "abc123def"
match = re.search(r'\d+', s)
if match:
    num = int(match.group())
    print(num)  # Output: 123

# /*================================================================

# 8. Handling Edge Cases
# It is essential to handle cases where the string cannot be directly converted to an integer, using try-except blocks.
s = "abc"
try:
    num = int(s)
except ValueError:
    num = None
print(num)  # Output: None