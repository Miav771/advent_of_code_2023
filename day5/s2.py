lines = open("input.txt").readlines()
seeds = lines[0].split()[1:]
ranges = [[int(seeds[i]), int(seeds[i + 1])] for i in range(0, len(seeds) - 1, 2)]

maps = [[]]
for line in lines[3:]:
    if line == "\n":
        continue
    if "map:" in line:
        maps[-1].sort(key=lambda x: x[1])
        maps.append([])
    else:
        maps[-1].append([int(value) for value in line.split()])

for map in maps:
    next_map_ranges = []
    for destination_range_start, source_range_start, map_range_length in map:
        # Each map contains individual mappings between ranges
        next_mapping_ranges = []
        for current_range_start, current_range_length in ranges:
            has_overlap = (
                source_range_start + map_range_length > current_range_start
                and current_range_start + current_range_length > source_range_start
            )
            if has_overlap:
                if current_range_start < source_range_start:
                    next_mapping_ranges.append(
                        [current_range_start, source_range_start - current_range_start]
                    )
                if (
                    current_range_start + current_range_length
                    > source_range_start + map_range_length
                ):
                    next_mapping_ranges.append(
                        [
                            source_range_start + map_range_length,
                            current_range_start
                            + current_range_length
                            - source_range_start
                            - map_range_length,
                        ]
                    )
                overlap_start = max(current_range_start, source_range_start)
                overlap_end = min(
                    current_range_start + current_range_length,
                    source_range_start + map_range_length,
                )
                new_range_length = overlap_end - overlap_start
                start_offset = overlap_start - source_range_start
                new_range_start = destination_range_start + start_offset
                next_map_ranges.append([new_range_start, new_range_length])
            else:
                next_mapping_ranges.append([current_range_start, current_range_length])
        ranges = next_mapping_ranges
    ranges += next_map_ranges
print(min([range[0] for range in ranges]))
