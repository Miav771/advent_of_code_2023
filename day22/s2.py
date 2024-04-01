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
block_supports = {idx: set() for idx in range(len(coordinates))}
block_supported_by = {}
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
    block_supported_by[idx] = supports
    for support in supports - {-1}:
        block_supports[support].add(idx)
    for y in range(start[0], end[0] + 1):
        for x in range(start[1], end[1] + 1):
            lz[y][x] = (resting_height + block_height, idx)

fallen_bricks = 0
for idx in block_supports.keys():
    removed = {idx}
    destabilized = block_supports[idx].copy()
    while destabilized:
        current_idx = destabilized.pop()
        if block_supported_by[current_idx].issubset(removed):
            removed.add(current_idx)
            destabilized |= block_supports[current_idx]
    fallen_bricks += len(removed) - 1
print(fallen_bricks)
