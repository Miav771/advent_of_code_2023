lines = tuple(tuple(line.strip()) for line in open("input.txt"))


def rotate_clockwise(lines):
    height, width = len(lines), len(lines[0])
    rotated_lines = []

    for y in range(width):
        rotated_lines.append(tuple(lines[x][y] for x in reversed(range(height))))
    return tuple(rotated_lines)


def score(lines):
    return sum(sum(i + 1 for i in range(len(line)) if line[i] == "O") for line in lines)


def shiftline(line):
    line = list(line)
    seen_moveable_rocks = 0
    for x in range(len(line)):
        if line[x] == "#":
            line[x - seen_moveable_rocks : x] = ["O"] * seen_moveable_rocks
            seen_moveable_rocks = 0
        elif line[x] == "O":
            line[x] = "."
            seen_moveable_rocks += 1
    if seen_moveable_rocks:
        line[-seen_moveable_rocks:] = ["O"] * seen_moveable_rocks
    return tuple(line)


def shift(lines):
    lines = list(lines)
    for y in range(len(lines)):
        lines[y] = shiftline(lines[y])
    return tuple(lines)


def cycle(lines):
    for _ in range(4):
        lines = shift(lines)
        lines = rotate_clockwise(lines)
    return lines


lines = rotate_clockwise(lines)
seen = set()
loop_start_iter = 1000000000 - 1
for i in range(1000000000):
    lines = cycle(lines)
    hashed = hash(lines)
    if hashed in seen:
        loop_start_iter = i
        break
    seen.add(hashed)

loop_data = [lines]
lines = cycle(lines)
while lines != loop_data[0]:
    loop_data.append(lines)
    lines = cycle(lines)

remaining_cycles = 1000000000 - loop_start_iter - 1
lines = loop_data[remaining_cycles % len(loop_data)]

print(score(lines))
