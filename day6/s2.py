from math import sqrt, ceil

lines = open("input.txt").readlines()
time = int("".join(lines[0].split()[1:]))
distance = int("".join(lines[1].split()[1:])) + 1

discriminant_root = sqrt(time**2 - 4 * distance)
min_hold = int(ceil((time - discriminant_root) / 2))
max_hold = int((time + discriminant_root) / 2)
hold_range = max_hold - min_hold + 1
print(hold_range)
