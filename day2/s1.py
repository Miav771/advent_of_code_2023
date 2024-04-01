possible_games = []
lim = {"red": 12, "green": 13, "blue": 14}
file = open("input.txt")
for idx, line in enumerate(file):
    game_id = idx + 1
    draws = line.split(":")[1].split(";")
    possible = True
    for draw in draws:
        colors = draw.split(",")
        for color_data in colors:
            value, color_name = color_data.strip().split(" ")
            if lim[color_name] < int(value):
                possible = False
    if possible:
        possible_games.append(game_id)
print(sum(possible_games))
