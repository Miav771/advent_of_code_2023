file = open("input.txt")

c_map = {"#": 1, ".": 0}


def get_reflections(pattern):
    columns = [0] * len(pattern[-1])
    rows = [0] * len(pattern)
    for y, row in enumerate(pattern):
        for x, char in enumerate(row):
            columns[x] |= c_map[char] << y
            rows[y] |= c_map[char] << x

    for mid in reversed(range(1, len(columns))):
        if (
            sum(
                (columns[mid + i] ^ columns[mid - i - 1]).bit_count()
                for i in range(min(mid, len(columns) - mid))
            )
            == 1
        ):
            return mid

    for mid in reversed(range(1, len(rows))):
        if (
            sum(
                (rows[mid + i] ^ rows[mid - i - 1]).bit_count()
                for i in range(min(mid, len(rows) - mid))
            )
            == 1
        ):
            return 100 * mid

    return 0


patterns = [[]]
for line in file:
    if line != "\n":
        patterns[-1].append(line.strip())
    else:
        patterns.append([])

print(sum(get_reflections(pattern) for pattern in patterns))
