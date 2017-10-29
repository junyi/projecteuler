import sys
import os
parentdir = os.path.abspath('../..')
sys.path.append(parentdir)
from itertools import permutations
from fractions import gcd

def is_nontrivial_cancelable(num, denom):
	# num = 'ab', denom = 'cd'
	# Either:
	# ab / cd -> a / d === num * d = denom * a
	# ab / cd -> b / c === num * c = denom * b

	a, b = [int(i) for i in str(num)]
	c, d = [int(i) for i in str(denom)]

	if b == c and d != 0 and num * d == denom * a:
		return True

	if a == d and c != 0 and num * c == denom * b:
		return True

	return False

def solve():
	nums = 1
	denoms = 1
	for num in xrange(10, 98):
		for denom in xrange(num + 1, 99):
			if is_nontrivial_cancelable(num, denom):
				nums *= num
				denoms *= denom

	return denoms / gcd(nums, denoms)

if __name__ == '__main__':
	ans = solve()
	print "Answer = ", ans
