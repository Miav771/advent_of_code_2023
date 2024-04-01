observation = open("input.txt").readlines()

x = 0
while x < len(observation[0]):
    for row in observation:
        if row[x] == "#":
            break
    else:
        for y in range(len(observation)):
            observation[y] = observation[y][: x + 1] + "." + observation[y][x + 1 :]
        x += 1
    x += 1

distance, y, galaxies = 0, 0, set()
for line in observation:
    for x, char in enumerate(line):
        if char == "#":
            distance += sum(abs(x - x2) + abs(y - y2) for y2, x2 in galaxies)
            galaxies.add((y, x))
    y += 1 + ("#" not in line)
print(distance)
