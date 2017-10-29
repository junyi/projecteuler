import sys
import os
parentdir = os.path.abspath('../..')
sys.path.append(parentdir)
from collections import defaultdict
from itertools import permutations, product

def pentagonal(n):
	return n * (3 * n - 1) / 2

def sorted_tuple(tup):
	return tuple(sorted(tup))

def solve():
	sums = {}
	i = 1
	prev_j, prev_k = i, i + 1
	while True:
		break_i = False
		x1 = pentagonal(i)
		j = max(i, prev_j) + 1
		while True:
			break_j = False
			x2 = pentagonal(j)
			k = max(j, prev_k) + 1
			while True:
				x3 = pentagonal(k)
				if x1 + x2 < x3:
					break_j = True
					break
				elif x1 + x2 == x3:
					print 'equal', x1, x2, x3, (i, j, k)
					prev_j, prev_k = j, k
					sums[(x1, x2)] = x3
					if (x2, x3) in sums or (x1, x3) in sums:
						print 'Found!', (x1, x2, x3)
					break_j = True
					break
				else:
					break

				k += 1
			if break_j:
				break
			j += 1
		if break_i:
			break
		i += 3

if __name__ == '__main__':
	ans = solve()
	print "Answer = ", ans
