file = open("input.txt")

coordinates = []
for line in file:
    coordinates.append(
        tuple(
            tuple(int(coordinate) for coordinate in point.split(","))
            for point in line.strip().split("~")
        )
    )
coordinates.sort(key=lambda points: points[0][2])
height = max(max(point[0][0], point[1][0]) for point in coordinates) + 1
width = max(max(point[0][1], point[1][1]) for point in coordinates) + 1
lz = [[(0, -1)] * width for _ in range(height)]
free_bricks = set(range(len(coordinates)))
for idx, points in enumerate(coordinates):
    start, end = points
    block_height = end[2] - start[2] + 1
    resting_height = max(
        lz[y][x][0]
        for y in range(start[0], end[0] + 1)
        for x in range(start[1], end[1] + 1)
    )
    supports = {
        lz[y][x][1]
        for y in range(start[0], end[0] + 1)
        for x in range(start[1], end[1] + 1)
        if lz[y][x][0] == resting_height
    }
    if len(supports) == 1:
        free_bricks -= supports
    for y in range(start[0], end[0] + 1):
        for x in range(start[1], end[1] + 1):
            lz[y][x] = (resting_height + block_height, idx)
print(len(free_bricks))
