import re

file = open("input.txt")
rule_pattern = re.compile(r"(\w+){|(\w)([<>])(\d+):(\w+)|(\w+)}")
part_pattern = re.compile(r"(\w)=(\d+)")

rules = dict()

for line in file:
    if line == "\n":
        break
    name, *rule_tokens = rule_pattern.findall(line)
    rules[name[0]] = [
        (rule[1], rule[2], int(rule[3]), rule[4]) for rule in rule_tokens[:-1]
    ] + [rule_tokens[-1][-1]]

accepted_sum = 0
for line in file:
    part = {attribute: int(rating) for attribute, rating in part_pattern.findall(line)}
    current_rule = "in"
    while current_rule not in "AR":
        for attribute, operator, threshold, next_rule in rules[current_rule][:-1]:
            if (part[attribute] < threshold and operator == "<") or (
                part[attribute] > threshold and operator == ">"
            ):
                current_rule = next_rule
                break
        else:
            current_rule = rules[current_rule][-1]
    if current_rule == "A":
        accepted_sum += sum(part.values())

print(accepted_sum)
