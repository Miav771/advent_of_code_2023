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


def getfront():
    for vertical in [-1, 0, 1]:
        for horizontal in [-1, 0, 1]:
            y, x = start[0] + vertical, start[1] + horizontal
            if (
                not (vertical == horizontal == 0)
                and 0 <= y < len(maze)
                and 0 <= x < len(maze[0])
                and (vertical, horizontal) in pipe_map[maze[y][x]]
            ):
                return ((y, x), (vertical, horizontal))


position, approach = getfront() or ((0, 0), (0, 0))
distance = 1
while position != start:
    distance += 1
    next_pipe = maze[position[0]][position[1]]
    approach = pipe_map[next_pipe][approach]
    position = (position[0] + approach[0], position[1] + approach[1])
print(distance // 2)
