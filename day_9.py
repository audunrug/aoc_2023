import numpy as np

def predict_next(seq, back=False):
	seq = [int(n) for n in seq]
	if back:
		seq.reverse()
	num_diff, diffs = seq, []
	diffs.append(num_diff)
	while set(num_diff) != {0}:
		num_diff = np.diff(num_diff)
		diffs.append(num_diff)
	for i in range(len(diffs)-2, -1, -1):
		diffs[i] = np.append(diffs[i], diffs[i][-1] + diffs[i+1][-1])
	return diffs[0][-1]

with open("input_9.txt") as file:
	seqs = [l.split(" ") for l in file.read().splitlines()]

# part 1
print(sum([predict_next(seq) for seq in seqs]))

# part 2
print(sum([predict_next(seq, back=True) for seq in seqs]))