import math

def next(nodes, node, dir):
	if dir == "L":
		return nodes[node][0]
	else:
		return nodes[node][1]

def walk(nodes, dirs):
	node, steps = 'AAA', 0
	while node != 'ZZZ':
		dir =  dirs[steps % len(dirs)]
		node = next(nodes, node, dir)
		steps += 1
	return steps

def walk_all(nodes, dirs):
    all_nodes = [n for n in nodes.keys() if n[2]=='A']
	#print([n for n in nodes.keys() if n[2]=='Z'])
    cycles = []
    for n in all_nodes:
         node_c = []
         nx, c = next(nodes, n, dirs[0]), 1
         while len(node_c) < 2:
             if nx[2] ==  'Z':
                 node_c.append(c)
                 c = 0
             dir =  dirs[c % len(dirs)]
             nx = next(nodes, nx, dir)
             c += 1
         if node_c[0] == node_c[1]:
             cycles.append(node_c[0])
         else: # dette er HELDIGVIS ikke tilfellet
             print("complex solution found")
    print(cycles)
    
    return(cycles)

with open("input_8.txt") as file:
	lines = file.read().splitlines()
sequence = list(lines[0])
nodes = {}
for l in lines[2:]:
	key, val = l.split(" = ")
	val = (val.split(", ")[0][1:], val.split(", ")[1][:-1])
	nodes[key] = val
	
print(walk(nodes, sequence))
print(math.lcm(*walk_all(nodes, sequence)))