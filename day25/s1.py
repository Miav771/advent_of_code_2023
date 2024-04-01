from random import choice
from collections import defaultdict

file = open("input.txt")
graph = defaultdict(set)
for line in file:
    origin, neighbors = line.strip().split(": ")
    neighbors = set(neighbors.split(" "))
    graph[origin] |= neighbors
    for neighbor in neighbors:
        graph[neighbor].add(origin)

graph = dict(graph)

# Kernighan-Lin + simulated annealing mutant
partition_a = {choice(list(graph.keys()))}
while len(partition_a) < len(graph) // 2:
    node = choice(list(partition_a))
    partition_a |= graph[node]
cuts = 0
partition_b = set(graph.keys()) - partition_a
iters = 1000
for i in range(iters):
    temp = 1 - i / iters
    candidates = []
    if len(partition_a) > 1:
        move_to_b_candidates = {
            node for node in partition_a if graph[node] - partition_a
        }
        for node in move_to_b_candidates:
            new_a = partition_a - {node}
            new_cuts = sum(len(graph[node] - new_a) for node in new_a)
            candidates.append((True, node, new_cuts))
    if len(partition_b) > 1:
        move_to_a_candidates = {
            node for node in partition_b if graph[node] - partition_b
        }
        for node in move_to_a_candidates:
            new_b = partition_b - {node}
            new_cuts = sum(len(graph[node] - new_b) for node in new_b)
            candidates.append((False, node, new_cuts))
    candidates.sort(key=lambda x: x[2])
    move_to_b, node, new_cuts = (
        candidates[0]
        if candidates[0][2] == 3
        else choice(candidates[: int(len(candidates) * temp) + 1])
    )
    if move_to_b:
        partition_a -= {node}
        partition_b |= {node}
        cuts = new_cuts
    else:
        partition_a |= {node}
        partition_b -= {node}
        cuts = new_cuts

    if i % 10 == 0:
        print(
            f"iter: {i}/{iters}, temp: {temp}, cuts: {cuts}, A: {len(partition_a)}, B: {len(partition_b)}"
        )
    if cuts == 3:
        break
print(
    f"cuts: {cuts}, A: {len(partition_a)}, B: {len(partition_b)}, A*B={len(partition_a)*len(partition_b)}"
)
