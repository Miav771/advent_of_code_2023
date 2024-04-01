file = open("input.txt")
total = []
for line in file:
    number_lists = line.split(":")[1].split("|")
    winning, selected = [set(numlist.split()) for numlist in number_lists]
    matches = len(winning & selected)
    if matches:
        total.append(2 ** (matches - 1))
print(sum(total))
