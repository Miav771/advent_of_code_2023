maze = open("input.txt").readlines()


def getstart():
    for y, row in enumerate(maze):
        for x, char in enumerate(row):
            if char == "S":
                return y, x


start = getstart() or (0, 0)  # Appease type-checker

pipe_map = {
    "|": {(1, 0): (1, 0), (-1, 0): (-1, 0)},
    "-": {(0, 1): (0, 1), (0, -1): (0, -1)},
    "L": {(1, 0): (0, 1), (0, -1): (-1, 0)},
    "J": {(1, 0): (0, -1), (0, 1): (-1, 0)},
    "7": {(-1, 0): (0, -1), (0, 1): (1, 0)},
    "F": {(-1, 0): (0, 1), (0, -1): (1, 0)},
    ".": {},
}

start_to_pipe = {
    frozenset(approach_map.values()): pipe for pipe, approach_map in pipe_map.items()
}

fronts = [
    ((y, x), (vertical, horizontal))
    for vertical in [-1, 0, 1]
    for horizontal in [-1, 0, 1]
    if not (vertical == horizontal == 0)
    and 0 <= (y := start[0] + vertical) < len(maze)
    and 0 <= (x := start[1] + horizontal) < len(maze[0])
    and (vertical, horizontal) in pipe_map[maze[y][x]]
]
approaches = frozenset({approach for position, approach in fronts})
maze[start[0]] = (
    maze[start[0]][: start[1]]
    + start_to_pipe[approaches]
    + maze[start[0]][start[1] + 1 :]
)
position, approach = fronts[0]
loop_tiles = set()

while position != start:
    loop_tiles.add(position)
    next_pipe = maze[position[0]][position[1]]
    approach = pipe_map[next_pipe][approach]
    position = (position[0] + approach[0], position[1] + approach[1])

enclosed_tiles = set()

for y, row in enumerate(maze):
    vertical_traversal_opener = None
    enclosed = False
    for x, pipe in enumerate(row):
        if (y, x) in loop_tiles:
            if (
                pipe == "|"
                or (vertical_traversal_opener == "L" and pipe == "7")
                or (vertical_traversal_opener == "F" and pipe == "J")
            ):
                enclosed = not enclosed
                vertical_traversal_opener = None
            if pipe in "LF":
                vertical_traversal_opener = pipe
        elif enclosed:
            enclosed_tiles.add((y, x))

print(len(enclosed_tiles))
