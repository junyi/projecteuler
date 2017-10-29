import sys
import os
parentdir = os.path.abspath('../..')
sys.path.append(parentdir)
from collections import defaultdict
from itertools import permutations, product

def to_num(perm):
	return int(''.join(str(i) for i in perm))

pandigital_set = set(xrange(0, 10))
def loop(divisibles, i, acc, result):
	acc_set = set(acc)
	if len(acc_set) != 9 - i:
		return

	if i == 0:
		missing_num = tuple(pandigital_set.difference(acc_set))
		result.append(missing_num + acc)
		return

	start_pair = acc[:2]
	if start_pair in divisibles[i - 1]:
		total = 0
		for (x1, _, _) in divisibles[i - 1][start_pair]:
			loop(divisibles, i - 1, (x1,) + acc, result)

def solve():
	divisors = [2, 3, 5, 7, 11, 13, 17]

	divisibles = defaultdict(lambda: defaultdict(set))
	for c, j in enumerate(divisors):
		for i in xrange(1000):
			if i % j == 0:
				x1, x2, x3 = map(int, list(str(i).zfill(3)))
				if x1 != x2 and x2 != x3 and x1 != x3:
					if c == 0 or (x1, x2) in divisibles[c - 1]:
						divisibles[c][(x2, x3)].add((x1, x2, x3))

	result = []
	total = 0
	last = len(divisibles) - 1
	for end in divisibles[last]:
		for triple in divisibles[last][end]:
			loop(divisibles, last, triple, result)

	for tup in result:
		total += to_num(tup)

	return total


if __name__ == '__main__':
	ans = solve()
	print "Answer = ", ans
