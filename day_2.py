import numpy as np
import pandas as pd

def sort_game(game):
	rounds = game.split("; ")
	game_res = {}
	for r in rounds:
		draws = r.split(", ")
		for d in draws:
			num, col = d.split(" ")
			#print(num, col)
			if col not in game_res.keys():
				game_res[col] = [int(num)]
			else:
				#print(game_res[col])
				game_res[col].append(int(num))
	return game_res

def get_game_max(game):
	game_dict, max_dict = sort_game(game), {}
	for col in ("red", "blue", "green"):
		if col in game_dict.keys():
			max_dict[col] = max(game_dict[col])
		else:
			max_dict[col] = 0
	return max_dict

def check_possible(game, goal):
	game_max = get_game_max(game)
	res = True
	for col in goal.keys():
		if goal[col] < game_max[col]:
			res = False
	return res

# for part 2
def get_cube_power(game):
	game_max, power = get_game_max(game), 1
	for val in game_max.values():
		power *= val

	return power




with open("input_2.txt") as file:
	games = file.read().splitlines()

# 1
goal = {"red": 12, "green": 13, "blue": 14}
results_1, results_2 = [], []
for g in games:
	print(g)
	game_n, game = g.split(": ")	
	print(get_game_max(game))
	print(get_cube_power(game))
	print("")
	if check_possible(game, goal):
		results_1.append(int(game_n.split(" ")[-1]))
	results_2.append(get_cube_power(game))
print(results_1)
print(results_2)

print(f"sum of possible games (p1): {sum(results_1)}")
print(f"sum of cube powers (p2): {sum(results_2)}")





