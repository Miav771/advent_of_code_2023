file = open("input.txt")

x,y = (0,0)
area = 0
boundary = 0
dir_map = {"U":(0,1), "D":(0,-1), "R":(1,0), "L":(-1,0)}
for line in file:
    dir, dist, _ = line.split()
    m_x, m_y = dir_map[dir]
    for _ in range(int(dist)):
        n_x, n_y = x+m_x, y+m_y
        # Shoelace theorem
        area += (n_x+x)*(n_y-y)
        boundary+=1
        x,y=n_x, n_y
print((abs(area)+ boundary)//2 + 1)
