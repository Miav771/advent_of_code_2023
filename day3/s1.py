schematic = open("input.txt").readlines()
max_y = len(schematic)
max_x = len(schematic[0])
numbers = []
for y, line in enumerate(schematic):
    num = 0
    valid = False
    for x, char in enumerate(line):
        if char.isdigit():
            num *= 10
            num += int(char)
            neighbors = {
                schematic[y + offset_y][x + offset_x]
                for offset_y in [-1, 0, 1]
                for offset_x in [-1, 0, 1]
                if not (offset_y == offset_x == 0)
                and 0 <= y + offset_y < max_y
                and 0 <= x + offset_x < max_x
            }
            valid |= any(neighbor not in "0123456789.\n" for neighbor in neighbors)
        else:
            if valid:
                numbers.append(num)
            num = 0
            valid = False
print(sum(numbers))
