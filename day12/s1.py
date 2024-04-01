file = open("input.txt")

arrangements_list = []
for line in file:
    records, lengths = line.strip().split()
    lengths = [int(length) for length in lengths.split(",")]
    arrangements = 0
    queue = [(records, lengths)]
    while queue:
        records, lengths = queue.pop()
        if not lengths:
            arrangements += "#" not in records
            continue
        records = records.lstrip(".")
        if not records:
            continue
        next_length = lengths[0]
        fits = (
            len(records) >= next_length
            and "." not in records[:next_length]
            and (len(records) == next_length or records[next_length] != "#")
        )
        must_fit = records[0] == "#"
        may_fit = records[0] == "?"
        if must_fit and not fits:
            continue
        if fits and (must_fit or may_fit):
            queue.append((records[next_length + 1 :], lengths[1:]))
        if not must_fit:
            queue.append((records[1:], lengths))
    arrangements_list.append(arrangements)


print(sum(arrangements_list))
