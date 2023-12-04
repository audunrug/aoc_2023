def get_card_points(card):
    card = [c.split(" ") for c in card.split("| ")]
    points = 0
    #print(card)
    for c in card[0]:
        if c in card[1] and c != '':
            if points == 0:
                points = 1
            else:
                points = points * 2
    return points

def get_new_cards(card):
    card = [c.split(" ") for c in card.split("| ")]
    new = 0
    #print(card)
    for c in card[0]:
        if c in card[1] and c != '':
            new += 1
    return new

def make_new_cards(cards, i, n):
    while n > 0:
        cards[i+n][1] += 1
        n -= 1
    return cards

with open("input_4.txt") as file:
	cards = file.read().splitlines()

# part 1
only_cards = [c.split(": ")[1] for c in cards]
all_points = [get_card_points(c) for c in only_cards]
print(f"Sum of all card points, part 1: {sum(all_points)}")

# part 2
cards_copies = [[get_new_cards(c), 1] for c in only_cards]
for i in range(len(cards_copies)):
    for c in range(cards_copies[i][1]):
        cards_copies = make_new_cards(cards_copies, i, cards_copies[i][0])

total_cards = [c[1] for c in cards_copies]
print(f"Total number of card copies, part 2: {sum(total_cards)}")
