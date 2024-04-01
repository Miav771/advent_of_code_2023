maze = [line.strip() for line in open("input.txt").readlines()]
height = len(maze)
width = len(maze[0])

start = (0, 0)
for y, row in enumerate(maze):
    for x, char in enumerate(row):
        if char == "S":
            start = (y, x)

queue = {start}
new_queue = set()
for _ in range(64):
    new_queue = set()
    while queue:
        c_y, c_x = queue.pop()
        neighbors = {
            (n_y, n_x)
            for m_y, m_x in [(1, 0), (0, 1), (-1, 0), (0, -1)]
            if 0 <= (n_y := c_y + m_y) < height
            and 0 <= (n_x := c_x + m_x) < width
            and maze[n_y][n_x] != "#"
        }
        new_queue |= neighbors

    queue = new_queue

for y, x in new_queue:
    maze[y] = maze[y][:x] + "O" + maze[y][x + 1 :]

print("\n".join(maze))

print(len(new_queue))
