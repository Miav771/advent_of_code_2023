observation = open("input.txt").readlines()
horizontal_modifier = [0] * len(observation[0])
x = 0
while x < len(observation[0]):
    for row in observation:
        if row[x] == "#":
            break
    else:
        for i in range(x, len(horizontal_modifier)):
            horizontal_modifier[i] += 1000000 - 1
    x += 1

distance, y, galaxies = 0, 0, set()
for line in observation:
    for x, char in enumerate(line):
        x += horizontal_modifier[x]
        if char == "#":
            distance += sum(abs(x - x2) + abs(y - y2) for y2, x2 in galaxies)
            galaxies.add((y, x))
    y += 1 + (1000000 - 1) * ("#" not in line)
print(distance)
