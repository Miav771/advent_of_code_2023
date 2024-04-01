from math import sqrt, ceil

lines = open("input.txt").readlines()
times = lines[0].split()[1:]
distances = lines[1].split()[1:]
assert len(times) == len(distances)
# We must break the record, so increment target distance
races_data = [(int(times[i]), int(distances[i]) + 1) for i in range(len(times))]

ranges = []
for time, distance in races_data:
    discriminant_root = sqrt(time**2 - 4 * distance)
    min_hold = int(ceil((time - discriminant_root) / 2))
    max_hold = int((time + discriminant_root) / 2)
    ranges.append((min_hold, max_hold))

cumulative_product = 1
for min_hold, max_hold in ranges:
    cumulative_product *= max_hold - min_hold + 1
print(cumulative_product)
