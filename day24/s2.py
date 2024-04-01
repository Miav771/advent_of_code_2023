# Sadly I had to resort to getting help from reddit on this one
# Wrote the below solution after reading reddit.com/r/adventofcode/comments/18q40he/2023_day_24_part_2_a_straightforward_nonsolver
# Though reasonably straightorward in retrospect, it didn't occur to me arrange a system of linear equations

file = open("input.txt")
hailstones = []
for line in file:
    start, velocity = line.strip().split(" @ ")
    hailstones.append(
        tuple(int(num) for num in start.split(", ") + velocity.split(", "))
    )


def gaussian_elimination(equations):
    assert len(equations) == len(equations[0]) - 1
    unknowns = len(equations[0]) - 1
    for i in range(unknowns - 1):
        current_equation = equations[i]
        current_equation_coefficient = current_equation[i]
        for n_i in range(i + 1, unknowns):
            next_equation_coefficient = equations[n_i][i]
            for p_i in range(i, unknowns + 1):
                equations[n_i][p_i] *= current_equation_coefficient
                equations[n_i][p_i] -= current_equation[p_i] * next_equation_coefficient
    results = [0] * unknowns
    for i in reversed(range(unknowns)):
        current_equation = equations[i]
        for o_c_i in range(i + 1, unknowns):
            current_equation[-1] -= current_equation[o_c_i] * results[o_c_i]
        results[i] = current_equation[-1] // current_equation[i]
    return results


"""
X + t*VX = x + t*vx
t*VX - t*vx = x - X
t*(VX - vx) = x - X
t = (x - X)/(VX-vx)
(x - X)/(VX - vx) = (y - Y)/(VY - vy)
(x - X)*(VY - vy) = (y - Y)*(VX - vx)
x*VY - x*vy - X*VY + X*vy = y*VX - y*vx - Y*VX + Y*vx
Y*VX - X*VY = x*vy - x*VY - X*vy + y*VX - y*vx + Y*vx
Y*VX - X*VY = X*(-vy) + Y*vx + VX*y + VY*(-x) + x*vy - y*vx
X*(-vy1) + Y*vx1 + VX*y1 + VY*(-x1) + x1*vy1 - y1*vx1 = X*(-vy2) + Y*vx2 + VX*y2 + VY*(-x2) + x2*vy2 - y2*vx2
X*(vy2-vy1) + Y*(vx1-vx2) + VX*(y1-y2) + VY*(x2-x1) = x2*vy2 - y2*vx2 - x1*vy1 + y1*vx1
"""

equationsXY, equationsXZ = [], []
for i in range(4):
    x1, y1, z1, vx1, vy1, vz1 = hailstones[i]
    x2, y2, z2, vx2, vy2, vz2 = hailstones[i + 1]
    equationsXY.append(
        [
            vy2 - vy1,
            vx1 - vx2,
            y1 - y2,
            x2 - x1,
            x2 * vy2 - y2 * vx2 - x1 * vy1 + y1 * vx1,
        ]
    )
    equationsXZ.append(
        [
            vz2 - vz1,
            vx1 - vx2,
            z1 - z2,
            x2 - x1,
            x2 * vz2 - z2 * vx2 - x1 * vz1 + z1 * vx1,
        ]
    )

X, Y, VX, VY = gaussian_elimination(equationsXY)
Xr, Z, VXr, VZ = gaussian_elimination(equationsXZ)
assert X == Xr and VX == VXr

print(X + Y + Z)
