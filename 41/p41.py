import sys
import os
parentdir = os.path.abspath('../..')
sys.path.append(parentdir)
from itertools import permutations
from projecteuler import prime

def to_num(perm):
	return int(''.join(str(i) for i in perm))

def solve():
	non_prime_digits = set([2, 4, 5, 6, 8, 0])
	perms = permutations(xrange(7, 0, -1))  # permutations of 1..8
	for perm in perms:
		if perm[-1] in non_prime_digits:
			continue

		# perm = (9,) + perm
		num = to_num(perm)
		if prime.is_prime(num):
			return num

if __name__ == '__main__':
	ans = solve()
	print "Answer = ", ans
