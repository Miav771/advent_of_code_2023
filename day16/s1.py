grid = [line.strip() for line in open("input.txt")]
height, width = len(grid), len(grid[0])
traversal_log = [[set() for _ in range(width)] for _ in range(height)]
traversal_log[0][0] = {(0, 1)}
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

queue = [(0, 0, (0, 1))]
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

print(sum(sum(bool(entry) for entry in row) for row in traversal_log))
