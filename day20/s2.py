from collections import deque, defaultdict
from math import lcm

file = open("input.txt")

start = ("", 0, [])
modules_map = {}
conjunction_state = {}
flop_state = {}
for line in file:
    module, next_modules = line.strip().split(" -> ")
    next_modules = next_modules.split(", ")
    if module == "broadcaster":
        start = ("broadcaster", 0, next_modules)
    else:
        type, module = module[0], module[1:]
        modules_map[module] = next_modules
        if type == "&":
            conjunction_state[module] = {}
        else:
            flop_state[module] = 0

conjunction_modules = set(conjunction_state.keys())
for module, next_modules in modules_map.items():
    if next_conjunctions := set(next_modules).intersection(conjunction_modules):
        for conjunction_module in next_conjunctions:
            conjunction_state[conjunction_module][module] = 0


queue = deque()
parent = [
    module for module, next_modules in modules_map.items() if "rx" in next_modules
][0]
dependency_activations = {
    module: [] for module, next_modules in modules_map.items() if parent in next_modules
}
iteration = 0
while not all(
    len(activation_timestamps) > 1
    for activation_timestamps in dependency_activations.values()
):
    iteration += 1
    queue.append(start)
    while queue:
        sender, current_pulse, current_modules = queue.popleft()
        if parent in current_modules and current_pulse:
            dependency_activations[sender].append(iteration)
        for current_module in current_modules:
            if current_module in conjunction_state:
                conjunction_state[current_module][sender] = current_pulse
                queue.append(
                    (
                        current_module,
                        int(not all(conjunction_state[current_module].values())),
                        modules_map[current_module].copy(),
                    )
                )
            elif not current_pulse:
                flop_state[current_module] = int(not flop_state[current_module])
                queue.append(
                    (
                        current_module,
                        flop_state[current_module],
                        modules_map[current_module].copy(),
                    )
                )

cycle_lengths = [end - start for start, end in dependency_activations.values()]
print(lcm(*cycle_lengths))
