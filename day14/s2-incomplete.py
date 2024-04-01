lines = [list(line.strip()) for line in open("example.txt")]
width = len(lines[0])
height = len(lines)

def rotate(lines, height, width):
    height, width = width, height
    rotated_lines = [[0]*width for _ in range(height)]

    for y in range(height):
        for x in range(width):
            rotated_lines[y][x] = lines[width-1-x][y]
    return rotated_lines, height, width


def shift(lines, height, width):
    for y in range(height):
        seen_moveable_rocks = 0
        for x in (range(width)):
            if lines[y][x] == "#":
                lines[y][x-seen_moveable_rocks:x] = ["O"]*seen_moveable_rocks
                seen_moveable_rocks = 0
            elif lines[y][x] == "O":
                lines[y][x] = "."
                seen_moveable_rocks+=1
        if seen_moveable_rocks:
            lines[y][-seen_moveable_rocks:] = ["O"]*seen_moveable_rocks
    return lines

for i in range(1000000000):
    if i % 1000 == 0:
        print(i/1000000000)
    lines, height, width = rotate(lines, height, width)
    lines = shift(lines, height, width)

print("\n".join(str(line) for line in lines))
