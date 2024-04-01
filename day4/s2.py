file = open("input.txt")
cards = []
for line in file:
    number_lists = line.split(":")[1].split("|")
    winning, selected = [set(numlist.split()) for numlist in number_lists]
    matches = len(winning & selected)
    cards.append(matches)

reps = [1] * len(cards)
for card_num, matches in enumerate(cards):
    for won_card_number in range(card_num + 1, card_num + 1 + matches):
        reps[won_card_number] += reps[card_num]
print(sum(reps))
