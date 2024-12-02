input = []
with open('input.txt', 'r') as f:
    for line in f:
        input.append(line.strip())

left_ids = []
right_ids = []

for x in input:
    ids = x.split(' ')
    left_ids.append(int(ids[0]))
    right_ids.append(int(ids[3]))

# PART 1
left_ids.sort()
right_ids.sort()

total_distance = 0
for i in range(len(left_ids)):
    total_distance += abs(left_ids[i] - right_ids[i])

print(total_distance)

# PART 2
total_similarity = 0
for i in range(len(left_ids)):
    total_similarity += right_ids.count(left_ids[i]) * left_ids[i]

print(total_similarity)