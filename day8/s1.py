lines = open("example.txt").readlines()
instructions = lines[0].strip()

network = {line[0:3]: {"L": line[7:10], "R": line[12:15]} for line in lines[2:]}
current = "AAA"
iteration_count = 0
while current != "ZZZ":
    current = network[current][instructions[iteration_count % len(instructions)]]
    iteration_count += 1
print(iteration_count)
