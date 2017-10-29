import sys
import os
parentdir = os.path.abspath('../..')
sys.path.append(parentdir)
from itertools import permutations

def check(multiplicand, multiplier, product):
	if int(multiplicand) * int(multiplier) != int(product):
		return False

	if set(multiplicand + multiplier + product) != set('123456789'):
		return False

	return True

def to_str(int_tuple):
	return ''.join([str(i) for i in int_tuple])

def perm_to_strs(perm, pos1, pos2):
	multiplicand = to_str(perm[:pos1])
	multiplier = to_str(perm[pos1:pos2])
	product = to_str(perm[pos2:])
	return multiplicand, multiplier, product

def solve():
	pandigital_set = set()
	all_perms = permutations(xrange(1, 10))
	for perm in all_perms:
		# Either
		# A * BBBB = CCCC
		# AA * BBB = CCCC
		for pos in (1, 2):
			multiplicand, multiplier, product = perm_to_strs(perm, pos, 5)
			if check(multiplicand, multiplier, product):
				pandigital_set.add(int(product))

	return sum(pandigital_set)

if __name__ == '__main__':
	ans = solve()
	print "Answer = ", ans
