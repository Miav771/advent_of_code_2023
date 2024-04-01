import re
from copy import deepcopy

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


accepted = []
queue = [
    (
        "in",
        {
            "x": [1, 4000],
            "m": [1, 4000],
            "a": [1, 4000],
            "s": [1, 4000],
        },
    )
]
while queue:
    current_name, current_constraints = queue.pop()
    for attribute, operator, threshold, next_rule in rules[current_name][:-1]:
        next_constraints = deepcopy(current_constraints)
        if operator == ">":
            next_constraints[attribute][0] = threshold + 1
            current_constraints[attribute][1] = threshold
        elif operator == "<":
            next_constraints[attribute][1] = threshold - 1
            current_constraints[attribute][0] = threshold

        if next_constraints[attribute][0] <= next_constraints[attribute][1]:
            if next_rule == "A":
                accepted.append(next_constraints)
            elif next_rule != "R":
                queue.append((next_rule, next_constraints))

        if not current_constraints[attribute][0] <= current_constraints[attribute][1]:
            break
    else:
        next_rule = rules[current_name][-1]
        if next_rule == "A":
            accepted.append(current_constraints)
        elif next_rule != "R":
            queue.append((next_rule, current_constraints))

combos = 0
for constraints in accepted:
    rule_combos = 1
    for minimum, maximum in constraints.values():
        rule_combos *= maximum - minimum + 1
    combos += rule_combos
print(combos)
