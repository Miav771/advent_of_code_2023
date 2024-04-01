file = open("input.txt")

x,y = (0,0)
area = 0
boundary = 0
dir_map = {"3":(0,1), "1":(0,-1), "0":(1,0), "2":(-1,0)}
for line in file:
    hexcode = line.split()[-1][2:-1]
    dist = int(hexcode[:-1],16)
    m_x, m_y = dir_map[hexcode[-1]]
    boundary+=dist
    n_x, n_y = x+m_x*dist, y+m_y*dist
    # Shoelace theorem
    area += (n_x+x)*(n_y-y)
    x,y=n_x, n_y

print((abs(area)+ boundary)//2 + 1)
