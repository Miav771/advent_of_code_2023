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

suitable_slopes = {(1, 0): "v", (0, 1): ">", (-1, 0): "^", (0, -1): "<"}

segments = dict()
queue = {start}
seen = set()

c_num = -1
while queue:
    c_num += 1
    c_num %= 10

    seg_start = queue.pop()
    neighbors = {seg_start} - seen
    length = 0
    while len(neighbors) == 1:
        seen |= neighbors
        c_y, c_x = neighbors.pop()
        neighbors = {
            (n_y, n_x)
            for m_y, m_x in [(1, 0), (0, 1), (-1, 0), (0, -1)]
            if 0 <= (n_y := c_y + m_y) < height
            and 0 <= (n_x := c_x + m_x) < width
            and (
                maze[n_y][n_x] == "."
                or maze[n_y][n_x] == suitable_slopes[(m_y, m_x)]
                or maze[n_y][n_x].isdigit()
            )
        }
        inflow_neighbors = {
            (n_y, n_x)
            for m_y, m_x in [(1, 0), (0, 1), (-1, 0), (0, -1)]
            if 0 <= (n_y := c_y + m_y) < height
            and 0 <= (n_x := c_x + m_x) < width
            and (maze[n_y][n_x] in ".<>^v" or maze[n_y][n_x].isdigit())
        } - neighbors
        outflow_segments = neighbors.intersection(segments.keys())
        neighbors -= seen
        if inflow_neighbors:
            segments[seg_start] = {
                "outflows": {(c_y, c_x)},
                "symbol": c_num,
                "length": length,
            }
            seg_start = (c_y, c_x)
            length = 0
            c_num += 1
            c_num %= 10
        length += 1
        maze[c_y] = maze[c_y][:c_x] + str(c_num) + maze[c_y][c_x + 1 :]

    if len(neighbors) > 1:
        queue |= neighbors
        segments[seg_start] = {"outflows": neighbors, "symbol": c_num, "length": length}
    elif (c_y, c_x) == end:
        segments[seg_start] = {"outflows": {end}, "symbol": c_num, "length": length}
    elif outflow_segments:
        segments[seg_start] = {
            "outflows": outflow_segments,
            "symbol": c_num,
            "length": length,
        }

print("\n".join(maze))
print(segments)

max_len = 0
queue = {(start,)}
while queue:
    current = queue.pop()
    last_node = segments[current[-1]]
    if end in last_node["outflows"]:
        max_len = max(max_len, sum(segments[node]["length"] for node in current))
    else:
        for outflow in last_node["outflows"] - set(current):
            queue.add(current + (outflow,))
print(max_len - 1)
