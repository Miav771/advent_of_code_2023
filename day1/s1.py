"""
The "correct" solution is to loop once from the front and then from the back, terminating on first match.
But it's simpler to just get all the digits in a list and then fetch the first and last one.
In AOC, I tend to capture as much data as I can to make debugging easy.
"""
nums = []
file = open("input.txt")
for line in file:
    line = line.strip()
    digits = []
    for char in line:
        if char.isdigit():
            digits.append(int(char))
    nums.append(digits[0] * 10 + digits[-1])
print(sum(nums))
