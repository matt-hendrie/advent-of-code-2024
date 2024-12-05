import re

input = []
with open('input.txt', 'r') as f:
    for line in f:
        input.append(line.strip())

regex_match = r'mul\(\d{1,3},\d{1,3}\)'
combined_pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"

# PART 1
total = 0
for x in input:
    matches = re.findall(regex_match, x)
    for match in matches:
        numbers = re.findall(r'\d{1,3}', match)
        total += int(numbers[0]) * int(numbers[1])
print(total)

# PART 2
process = True
total = 0
for x in input:
    matches = re.finditer(combined_pattern, x)
    for match in matches:
        if match.group() == 'do()':
            process = True
        elif match.group() == "don't()":
            process = False
        else:
            numbers = re.findall(r'\d{1,3}', match.group())
            if process:
                total += int(numbers[0]) * int(numbers[1])
print(total)