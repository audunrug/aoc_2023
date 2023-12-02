import numpy as np
import pandas as pd
import requests as req  # the lib that handles the url stuff

with open("input_1.txt") as file:
	lines = file.read().splitlines()

# 1
values = []
for line in lines:
	ns = []
	for n in line:
		#print(n)
		try:
			t = int(n)
			ns.append(n)
		except ValueError:
			continue

	values.append(int(ns[0]+ns[-1]))

print(f"sum of letter values part 1: {sum(values)}")

# 2
en_num =  {
"one": "1",
"two": "2",
"three": "3",
"four": "4",
"five": "5",
"six": "6",
"seven": "7",
"eight": "8",
"nine": "9"
}
values_2 = []
for line in lines:
	first, last = [100, 100], [-1, -1]
	#print(line)

	for key in en_num.keys():
		n = en_num[key]
		#line_n = line.replace(key, n)
		if line.find(n) != -1 and line.find(key) != -1:
			first_n = min(line.find(n), line.find(key))
		elif line.find(n) != -1:
			first_n = line.find(n)
		elif line.find(key) != -1:
			first_n = line.find(key)
		else:
			first_n = -1
		last_n =  max(line.rfind(n), line.rfind(key))
		
		if first_n != -1 and first_n < first[1]:
			first = [n, first_n] 
		if last_n != -1 and last_n > last[1]:
			last = [n, last_n] 


	#print(f"sum: {int(first[0]+last[0])}")
	#print("")
	values_2.append(int(first[0]+last[0]))

#print(values)
print(f"sum of letter values part 2: {sum(values_2)}")
