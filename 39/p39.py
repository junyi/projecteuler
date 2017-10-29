import sys
import os
parentdir = os.path.abspath('../..')
sys.path.append(parentdir)
import math

def solve():
	MAX = 1001
	max_solutions = 0
	arg_max = 0
	"""
		Combine triangle inequality, perimeter and right triangle constraint
		Also assume a <= b <= c for symmetry
	"""
	for n in xrange(3, MAX):
		solution_count = 0
		for a in xrange(1, int(n / 2) + 1):
			for b in xrange(a, int(n / 2) + 1):
				c = n - a - b
				if a + b <= n / 2. or c < b:
					continue
				if a ** 2 + b ** 2 - c ** 2 != 0:
					continue
				solution_count += 1

		if solution_count > max_solutions:
			max_solutions = solution_count
			arg_max = n

	return arg_max, max_solutions

if __name__ == '__main__':
	ans = solve()
	print "Answer = ", ans
