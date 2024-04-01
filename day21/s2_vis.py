maze = [(line.strip()[:-1] + "|") * 9 for line in open("input.txt").readlines()]
maze[-1] = "-" * len(maze[-1])
maze *= 9
height = len(maze)
width = len(maze[0])


def get_reachable_plots(moves, startpoint):
    queue = {startpoint}
    new_queue = set()
    for i in range(moves):
        if i % 10 == 0:
            print(f"{i}/{moves}")
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
    return new_queue


new_queue = get_reachable_plots(65 + 131 * 2, (131 * 4 + 65, 131 * 4 + 65))
for y, x in new_queue:
    maze[y] = maze[y][:x] + "O" + maze[y][x + 1 :]

print("\n".join(maze))
print(len(new_queue))
