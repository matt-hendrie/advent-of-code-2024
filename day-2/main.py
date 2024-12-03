from tabnanny import check

import numpy as np

input = []
with open('input.txt', 'r') as f:
    for line in f:
        input.append(line.strip())

def check_levels(diff):
    current_safe = True
    if any(diff < 0) and any(diff > 0):
        current_safe = False
    for i in diff:
        if abs(i) < 1 or abs(i) > 3:
            current_safe = False
            break
    return current_safe

# PART 1
safe_count = 0
for x in input:
    levels = x.split(' ')
    levels = list(map(int, levels))
    diff = np.diff(levels)
    if check_levels(diff):
        safe_count += 1

print(safe_count)

# PART 2
fixed_safe_count = 0
for x in input:
    levels = x.split(' ')
    levels = list(map(int, levels))
    fail_count = 0
    diff = np.diff(levels)
    if check_levels(diff):
        fixed_safe_count += 1
    else:
        # Remove current level and try again
        for i in range(len(levels)):
            temp = levels.copy()
            temp.pop(i)
            diff = np.diff(temp)
            if check_levels(diff):
                fixed_safe_count += 1
                break
print(fixed_safe_count)
