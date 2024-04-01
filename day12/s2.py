from collections import Counter
from functools import lru_cache

file = open("input.txt")

@lru_cache(maxsize=512)
def arrangement_count(records, lengths):
    if not lengths:
        return int("#" not in records)
    records = records.lstrip(".")
    if not records or len(records) < sum(lengths) + len(lengths) - 1:
        return 0
    next_length = lengths[0]
    fits = (
        len(records) >= next_length
        and "." not in records[:next_length]
        and (len(records) == next_length or records[next_length] != "#")
    )
    must_fit = records[0] == "#"
    may_fit = records[0] == "?"
    if must_fit and not fits:
        return 0
    arrangements = 0
    if fits and (must_fit or may_fit):
        arrangements += arrangement_count(records[next_length + 1 :], lengths[1:])

    if not must_fit:
        arrangements += arrangement_count(records[1:], lengths)
    return arrangements


arrangements_list = []
for (line_number, line) in enumerate(file):
    records, lengths = line.strip().split()
    records = "?".join([records] * 5)
    lengths = tuple([int(length) for length in lengths.split(",")] * 5)
    arrangements = arrangement_count(records, lengths)
    print(f"Finished line {line_number+1}")
    arrangements_list.append(arrangements)


print(sum(arrangements_list))
