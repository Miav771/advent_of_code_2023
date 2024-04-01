from collections import Counter

file = open("input.txt")

card_scores = {"T": 10, "J": 1, "Q": 12, "K": 13, "A": 14} | {
    str(i): i for i in range(2, 10)
}

scores_and_bids = []
for line in file:
    cards, bid = line.split()
    counter = Counter(cards)
    jokers = counter["J"]
    del counter["J"]
    occurences = [occurence_count for _, occurence_count in counter.most_common()] + [
        0,
        0,
    ]
    score = ((occurences[0] + jokers) << 3) + occurences[1]
    for card in cards:
        score = score << 4
        score = score | card_scores[card]
    scores_and_bids.append((score, int(bid)))
scores_and_bids.sort()
ranks_and_bids = [
    (idx + 1, score_and_bid[1]) for idx, score_and_bid in enumerate(scores_and_bids)
]
print(sum(rank * bid for rank, bid in ranks_and_bids))
