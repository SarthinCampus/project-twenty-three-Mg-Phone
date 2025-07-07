import re

text = input()

# This pattern matches integers and decimal numbers (e.g., 123, 4.56)
numbers = re.findall(r'\d+(?:\.\d+)?', text)

for num in numbers:
    print(num)
