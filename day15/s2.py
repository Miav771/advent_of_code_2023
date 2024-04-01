lines = open("input.txt")


def hash(string):
    val = 0
    for char in string:
        val += ord(char)
        val *= 17
        val %= 256
    return val


boxes = [dict() for _ in range(256)]

for line in lines:
    for step in line.strip().split(","):
        if step[-1].isdigit():
            focal_length = int(step[-1])
            label = step[:-2]
            idx = hash(label)
            boxes[idx][label] = focal_length
        else:
            label = step[:-1]
            idx = hash(label)
            if label in boxes[idx]:
                del boxes[idx][label]

print(
    sum(
        sum(
            (focal_length * (box_num + 1) * (slot_in_box + 1))
            for slot_in_box, focal_length in enumerate(box.values())
        )
        for box_num, box in enumerate(boxes)
    )
)
