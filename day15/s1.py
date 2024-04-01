lines = open("input.txt")


def hash(string):
    val = 0
    for char in string:
        val += ord(char)
        val *= 17
        val %= 256
    return val


hashes = []
for line in lines:
    for step in line.strip().split(","):
        hashes.append(hash(step))

print(sum(hashes))
