"""
The from-scratch solution is to create a state machine for matching the digits.
Figured I'd use regex to make my life easier and got caught in everyone's favourite trap
of my solution working on the example, but not full input.
Reason is, regex searches greedily and so doesn't work for overlapping digits.
Like, "5sevenine" is gonna end up with matches of "5" and "seven".
Used a lookahead capture group as a quick workaround.
"""
import re

regex = r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))"
file = open("input.txt")
nums = []
digit_mapping = {
    name: idx + 1
    for idx, name in enumerate(
        ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    )
} | {str(num): num for num in range(1, 10)}
for line in file:
    line = line.strip()
    raw_digits = re.findall(regex, line)
    digits = [digit_mapping[raw_digit] for raw_digit in raw_digits]
    nums.append(digits[0] * 10 + digits[-1])
print(sum(nums))
