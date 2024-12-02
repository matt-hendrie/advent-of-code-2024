import numpy as np

input = []
with open('input.txt', 'r') as f:
    for line in f:
        input.append(line.strip())

# PART 1
safe_levels = 0
for x in input:
    levels = x.split(' ')
    levels = list(map(int, levels))
    current_safe = True
    diff = np.diff(levels)
    # check if diff only contains positives or negatives
    if any(diff < 0) and any(diff > 0):
        current_safe = False
    for i in diff:
        if abs(i) < 1 or abs(i) > 3:
            current_safe = False
            break
    if current_safe:
        safe_levels += 1

print(safe_levels)
