lines = open("input.txt").readlines()
seeds = [int(seed) for seed in lines[0].split()[1:]]

maps = [[]]
for line in lines[3:]:
    if line == "\n":
        continue
    if "map:" in line:
        maps[-1].sort(key=lambda x: x[1])
        maps.append([])
    else:
        maps[-1].append([int(value) for value in line.split()])

location_numbers = []
for seed in seeds:
    for map in maps:
        for destination_range_start, source_range_start, range_length in map:
            if source_range_start <= seed < source_range_start + range_length:
                offset = seed - source_range_start
                seed = destination_range_start + offset
                break

    location_numbers.append(seed)
print(min(location_numbers))
