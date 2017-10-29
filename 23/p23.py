import sys
import os
parentdir = os.path.abspath('../..')
sys.path.append(parentdir)
from projecteuler.prime import divisors

def is_abundant(num):
	return sum(divisors(num)) - num > num

def solve(limit=28124):
	abundants = set()
	for i in xrange(1, limit):
		if is_abundant(i):
			abundants.add(i)

	non_abundant_sum = 0

	for i in xrange(1, limit):
		abundant_sum = False
		for j in xrange(12, i):
			if (i - j) in abundants and j in abundants:
				abundant_sum = True
				break

		if not abundant_sum:
			non_abundant_sum += i

	return non_abundant_sum

if __name__ == '__main__':
	ans = solve()
	print "Answer = ", ans
