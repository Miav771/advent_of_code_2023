maze = [line.strip() for line in open("input.txt").readlines()]
height = len(maze)
width = len(maze[0])

start = (0, 0)
for x, char in enumerate(maze[0]):
    if char == ".":
        start = (0, x)

end = (0, 0)
for x, char in enumerate(maze[-1]):
    if char == ".":
        end = (height - 1, x)

junctions_and_neighbors = {
    start: {(start[0] + 1, start[1])},
    end: {(end[0] - 1, end[1])},
} | {
    (y, x): neighbors
    for y in range(height)
    for x in range(width)
    if maze[y][x] in ".<>^v"
    and len(
        neighbors := [
            (n_y, n_x)
            for m_y, m_x in [(1, 0), (0, 1), (-1, 0), (0, -1)]
            if 0 <= (n_y := y + m_y) < height
            and 0 <= (n_x := x + m_x) < width
            and (maze[n_y][n_x] in ".<>^v")
        ]
    )
    > 2
}

junctions = {}
queue = set()
for junction, neighbors in junctions_and_neighbors.items():
    junctions[junction] = set()
    queue |= {(junction, neighbor) for neighbor in neighbors}

for idx, current in enumerate(queue):
    origin_junction, current = current
    path = {origin_junction}
    neighbors = {current}
    while current not in junctions:
        y, x = current
        maze[y] = maze[y][:x] + str(idx%10) + maze[y][x + 1 :]
        path.add(current)
        neighbors = {
            (n_y, n_x)
            for m_y, m_x in [(1, 0), (0, 1), (-1, 0), (0, -1)]
            if 0 <= (n_y := y + m_y) < height
            and 0 <= (n_x := x + m_x) < width
            and (maze[n_y][n_x] in ".<>^vX" or maze[n_y][n_x].isdigit())
        } - path
        assert len(neighbors) == 1
        current = neighbors.pop()
    assert current in junctions
    junctions[origin_junction].add((current, len(path)))


for c_y, c_x in junctions.keys():
    maze[c_y] = maze[c_y][:c_x] + "X" + maze[c_y][c_x + 1 :]

print("\n".join(maze))
print({junction: len(neighbors) for junction, neighbors in junctions.items()})
print(junctions)

max_len = 0
queue = [(0, [start])]
while queue:
    current_length, current_path = queue.pop()
    head = current_path[-1]
    if head == end and current_length > max_len:
        max_len = current_length
        print(max_len)
    else:
        for junction, distance_to_junction in sorted(junctions[head], key= lambda neighbor: neighbor[1]):
            if junction not in current_path:
                queue.append((current_length+distance_to_junction, current_path+[junction] ) )
print(max_len)
