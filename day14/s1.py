lines = open("input.txt").readlines()
width = len(lines[0].strip())
height = len(lines)
load = 0
last_rock_position = [0] * width
rounded_rocks_seen = [0] * width

for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == "#":
            load += (height - last_rock_position[x]) * rounded_rocks_seen[x] - (
                rounded_rocks_seen[x] - 1
            ) * (rounded_rocks_seen[x]) // 2
            last_rock_position[x] = y + 1
            rounded_rocks_seen[x] = 0
        elif char == "O":
            rounded_rocks_seen[x] += 1

for x in range(width):
    load += (height - last_rock_position[x]) * rounded_rocks_seen[x] - (
        rounded_rocks_seen[x] - 1
    ) * (rounded_rocks_seen[x]) // 2

print(load)
