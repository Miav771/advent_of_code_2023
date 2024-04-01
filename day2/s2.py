# An extremely silly function that I wrote cause I was curious if it'd work
def mul(iterable):
    return eval("*".join(str(item) for item in iterable))


limits = []
file = open("input.txt")
for line in file:
    draws = line.split(":")[1].split(";")
    limit = {"red": 0, "green": 0, "blue": 0}
    for draw in draws:
        colors = draw.split(",")
        for color_data in colors:
            value, color_name = color_data.strip().split(" ")
            limit[color_name] = max(limit[color_name], int(value))
    limits.append(limit)
powers = [mul(limit.values()) for limit in limits]
print(sum(powers))
