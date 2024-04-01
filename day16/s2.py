grid = [line.strip() for line in open("input.txt")]
height, width = len(grid), len(grid[0])

mirror_map = {
    "|": {
        (1, 0): {(1, 0)},
        (-1, 0): {(-1, 0)},
        (0, 1): {(1, 0), (-1, 0)},
        (0, -1): {(1, 0), (-1, 0)},
    },
    "-": {
        (0, 1): {(0, 1)},
        (0, -1): {(0, -1)},
        (1, 0): {(0, 1), (0, -1)},
        (-1, 0): {(0, 1), (0, -1)},
    },
    "\\": {(1, 0): {(0, 1)}, (0, -1): {(-1, 0)}, (-1, 0): {(0, -1)}, (0, 1): {(1, 0)}},
    "/": {(1, 0): {(0, -1)}, (0, 1): {(-1, 0)}, (-1, 0): {(0, 1)}, (0, -1): {(1, 0)}},
    ".": {(1, 0): {(1, 0)}, (-1, 0): {(-1, 0)}, (0, 1): {(0, 1)}, (0, -1): {(0, -1)}},
}

visgrid = grid.copy()

starting_points = (
    [(y, 0, (0, 1)) for y in range(height)]
    + [(y, width - 1, (0, -1)) for y in range(height)]
    + [(0, x, (1, 0)) for x in range(width)]
    + [(height - 1, x, (-1, 0)) for x in range(width)]
)

energisation = []
for i, starting_point in enumerate(starting_points):
    traversal_log = [[set() for _ in range(width)] for _ in range(height)]
    traversal_log[starting_point[0]][starting_point[1]] = {starting_point[2]}
    queue = [starting_point]
    while queue:
        y, x, approach = queue.pop()
        next_approaches = mirror_map[grid[y][x]][approach]
        for approach in next_approaches:
            next_y, next_x = y + approach[0], x + approach[1]
            if (
                0 <= next_y < height
                and 0 <= next_x < width
                and approach not in traversal_log[next_y][next_x]
            ):
                queue.append((next_y, next_x, approach))
                traversal_log[next_y][next_x].add(approach)
    print(f"{i+1}/{len(starting_points)}")
    energisation.append(sum(sum(bool(entry) for entry in row) for row in traversal_log))
print(max(energisation))
