from math import lcm

lines = open("input.txt").readlines()
instructions = lines[0].strip()

network = {line[0:3]: {"L": line[7:10], "R": line[12:15]} for line in lines[2:]}
current = [node for node in network.keys() if node[-1] == "A"]
periods = []
iteration_count = 0
while current:
    current = [
        network[node][instructions[iteration_count % len(instructions)]]
        for node in current
    ]
    iteration_count += 1
    if iteration_count % len(instructions) == 0:
        filtered = [node for node in current if node[-1] != "Z"]
        if len(filtered) != len(current):
            current = filtered
            periods.append(iteration_count)
print(lcm(*periods))
