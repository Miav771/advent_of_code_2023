schematic = open("input.txt").readlines()
max_y = len(schematic)
max_x = len(schematic[0])
gears = []


def expand_coordinates(coords):
    y, x = coords
    start, end = x, x
    line = schematic[y]
    while line[start - 1].isdigit():
        start -= 1
    while line[end].isdigit():
        end += 1
    return (y, (start, end))


for y, line in enumerate(schematic):
    for x, char in enumerate(line):
        if char == "*":
            neighbors = {
                expand_coordinates((y + offset_y, x + offset_x))
                for offset_y in [-1, 0, 1]
                for offset_x in [-1, 0, 1]
                if not (offset_y == offset_x == 0)
                and 0 <= y + offset_y < max_y
                and 0 <= x + offset_x < max_x
                and schematic[y + offset_y][x + offset_x].isdigit()
            }
            if len(neighbors) == 2:
                gears.append(
                    [int(schematic[c[0]][c[1][0] : c[1][1]]) for c in neighbors]
                )
print(sum(l * r for l, r in gears))
