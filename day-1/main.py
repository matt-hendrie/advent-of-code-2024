input = []
with open('input.txt', 'r') as f:
    for line in f:
        input.append(line.strip())

left_ids = []
right_ids = []

for x in input:
    ids = x.split(' ')
    left_ids.append(ids[0])
    right_ids.append(ids[3])

# PART 1
left_ids.sort()
right_ids.sort()

total_distance = 0
for i in range(len(left_ids)):
    total_distance += abs(int(left_ids[i]) - int(right_ids[i]))

print(total_distance)

# PART 2
total_similarity = 0
for i in range(len(left_ids)):
    occur = 0
    for x in range(len(right_ids)):
        if left_ids[i] == right_ids[x]:
            occur += 1
    total_similarity += int(left_ids[i]) * occur

print(total_similarity)