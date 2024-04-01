grid = [[int(dist) for dist in line.strip()] for line in open("input.txt")]
height, width = len(grid), len(grid[0])
approaches = {(-1, 0), (1, 0), (0, 1), (0, -1)}
min_loss_per_approach = [
    [{approach: [2**31] * 10 for approach in approaches} for _ in range(width)]
    for _ in range(height)
]
min_loss_per_approach[0][0] = {approach: [0] + [2**31] * 9 for approach in approaches}

start = (0, 0)
iter_count = 0
queue = [start]
while queue:
    iter_count += 1
    if iter_count % 5000 == 0:
        print(f"Queue size: {len(queue)}/{height*width}")

    c_y, c_x = queue.pop()
    for a_y, a_x, n_y, n_x in [
        (a_y, a_x, n_y, n_x)
        for a_y, a_x in approaches
        if 0 <= (n_y := c_y + a_y) < height and 0 <= (n_x := c_x + a_x) < width
    ]:
        min_loss_reduced = False

        # Taking a turn
        turn_loss = min(
            min(min_loss_per_approach[c_y][c_x][approach][3:]) + grid[n_y][n_x]
            for approach in approaches - {(a_y, a_x), (-a_y, -a_x)}
        )
        if turn_loss < min_loss_per_approach[n_y][n_x][(a_y, a_x)][0]:
            min_loss_per_approach[n_y][n_x][(a_y, a_x)][0] = turn_loss
            min_loss_reduced = True

        for line_length, loss in enumerate(
            min_loss_per_approach[c_y][c_x][(a_y, a_x)][:4]
        ):
            line_length += 1
            loss += grid[n_y][n_x]
            if loss < min_loss_per_approach[n_y][n_x][(a_y, a_x)][line_length]:
                min_loss_per_approach[n_y][n_x][(a_y, a_x)][line_length] = loss
                min_loss_reduced = True

        for line_length, loss in enumerate(
            min_loss_per_approach[c_y][c_x][(a_y, a_x)][4:9]
        ):
            line_length += 5
            loss += grid[n_y][n_x]
            if loss < min_loss_per_approach[n_y][n_x][(a_y, a_x)][line_length]:
                min_loss_per_approach[n_y][n_x][(a_y, a_x)][line_length] = loss
                min_loss_reduced = True

        if min_loss_reduced:
            queue.append((n_y, n_x))

    queue.sort(
        reverse=True,
        key=lambda pos: min(
            min(losses) for losses in min_loss_per_approach[pos[0]][pos[1]].values()
        ),
    )

print(
    min(
        min(losses[4:])
        for losses in min_loss_per_approach[height - 1][width - 1].values()
    )
)
