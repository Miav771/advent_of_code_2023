from collections import deque

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

modules_with_output = set(modules_map.keys())
conjunction_modules = set(conjunction_state.keys())
for module, next_modules in modules_map.items():
    if next_conjunctions := set(next_modules).intersection(conjunction_modules):
        for conjunction_module in next_conjunctions:
            conjunction_state[conjunction_module][module] = 0

queue = deque()
pulses = [0, 0]
for i in range(1000):
    pulses[0] += 1
    queue.append(start)
    while queue:
        sender, current_pulse, current_modules = queue.popleft()
        pulses[current_pulse] += len(current_modules)
        current_modules = [
            current_module
            for current_module in current_modules
            if current_module in modules_with_output
        ]
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

print(pulses[0] * pulses[1])
