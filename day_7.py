num_card = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
num_card_j = num_card
num_card_j['J'] = 1

def convert_hand(hand, J=False):
    h = [*hand]
    #print(h)
    for i in range(len(h)):
        if h[i] in num_card.keys():
            if J:
    	        h[i] = num_card_j[h[i]]
            else:   
    	        h[i] = num_card[h[i]]
        else:
            h[i] = int(h[i])
    return h
    
def get_type(h, J=False):
    if J == False:
        counts = [h.count(v) for v in set(h)]
        mc = max(counts)
        if mc == 5:
            type = 7
        elif mc == 4:
            type = 6
        elif set(counts) == {2, 3}:
            type = 5
        elif mc == 3:
            type = 4
        elif sorted(counts) == [1, 2, 2]:
            type = 3
        elif 2 in counts:
            type = 2
        else:
            type = 1
    else:
        js = h.count("J")
        if js > 0:
            h = h.replace("J","")
            counts = [h.count(v) for v in set(h)]
            if counts != []:
                mc = max(counts)
            else:
                mc = 0
            if mc + js == 5:
                type = 7
            elif mc + js == 4:
                type = 6
            elif (js == 1 and counts == [2, 2]) or (set(counts) == {2, 3}):
                type = 5
            elif mc + js == 3:
                type = 4
            elif sorted(counts) == [1, 2, 2]:
                type == 3
            elif mc + js == 2:
                type = 2
            else:
                type = 1
        else:
            type = get_type(h, J=False)
    return type

def sort_hands(hands, J=False):
    sorts = []
    for h in hands:
         if J:
            sorts.append((get_type(h, J=1), convert_hand(h, J=1), h))
         else:
            sorts.append((get_type(h, J=0), convert_hand(h, J=0), h))
    sorts = sorted(sorts)
    return(sorts)

with open("input_7.txt") as file:
	lines = file.read().splitlines()
bids = {}
for l in lines:
	g = l.split(" ")
	bids[g[0]] = int(g[1])

# part 1
srt, w = sort_hands(bids.keys(),J=0), 0
for i in range(len(srt)):
    w += bids[srt[i][2]] * (i+1)
print(w)

# part 2
srt, w = sort_hands(bids.keys(), J=1), 0
for i in range(len(srt)):
    w += bids[srt[i][2]] * (i+1)
print(w)