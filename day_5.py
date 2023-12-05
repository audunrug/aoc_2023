def seed_to_loc(seed, maps):
    for m in maps:
        for r in m.keys():
            if seed in r:
                seed += m[r]
                break
    return seed

def convert_range(sr, m):
    #print(sr)
    nr, left = [], sr
    for r in m.keys():
        if sr.start >= r.start and sr.stop <= r.stop:
            #print(f"{sr} in {r}")
            return range(sr.start + m[r], sr.stop + m[r])
        elif left.start in r and not left.stop in r:
            #print(f"{left} partially in {r}")
            nr.append(range(left.start + m[r], r.stop + m[r]))
            left = range(r.stop, left.stop)
        elif left.start not in r and left.stop in r:
            #print(f"{left} partially in {r}")
            nr.append(range(r.start + m[r], left.stop + m[r]))
            left = range(left.start, r.start)
    if left.stop != left.start:
        nr.append(left)
    return nr

def s_range_to_locs(r, maps):
    #print(r)
    overlaps = 0
    for m in maps:
        #print(m)
        if not isinstance(r, list):
            r = convert_range(r, m)
        else:
            new = []
            for i in r:
                nr = convert_range(i, m)
                if not isinstance(nr, list):
                    new.append(nr) # so that it doesnt unpack single ranges
                else:
                    new.extend(nr)
            r = new
        #print("converted to", r)
    return r

with open("input_5.txt") as file:
	lines = file.read().splitlines()
maps = []
for line in lines:
    if line == "":
        maps.append({})
    elif len(line.split(" ")) == 3:
        v = [int(i) for i in line.split(" ")]
        maps[-1][range(v[1], v[1]+v[2])] = v[0]-v[1]

# part 1
seeds = [int(i) for i in lines[0].split(" ")[1:]]
locs = [seed_to_loc(s, maps) for s in seeds]
print(f"Lowest location number (p1):  {min(locs)}")

# part 2
srs = [range(seeds[n], seeds[n]+seeds[n+1]) for n in range(0, len(seeds), 2)]
loc_ranges = [s_range_to_locs(sr, maps) for sr in srs]
starts = [l.start for loc in loc_ranges for l in loc]
print(f"Lowest location number (p2):  {min(starts)}")