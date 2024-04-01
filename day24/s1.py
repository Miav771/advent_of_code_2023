file = open("input.txt")
hailstones = []
for line in file:
    start, velocity = line.strip().split(" @ ")
    hailstones.append(
        tuple(int(num) for num in start.split(", ") + velocity.split(", "))
    )

combos = {}
intersections = 0
for i in range(len(hailstones) - 1):
    for j in range(i + 1, len(hailstones)):
        x1, y1, _, vx1, vy1, _ = hailstones[i]
        x2, y2, _, vx2, vy2, _ = hailstones[j]
        slope1, slope2 = vy1 / vx1, vy2 / vx2
        if slope1 == slope2:
            combos[(i, j)] = None
            continue
        x = (y2 - y1 + slope1 * x1 - slope2 * x2) / (slope1 - slope2)
        t1 = (x - x1) / vx1
        t2 = (x - x2) / vx2
        y = slope1 * (x - x1) + y1
        intersections += (
            200000000000000 <= x <= 400000000000000
            and 200000000000000 <= y <= 400000000000000
            and t1 >= 0
            and t2 >= 0
        )
        combos[(i, j)] = (x, y, t1, t2)


print(intersections)
