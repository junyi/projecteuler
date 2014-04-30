from fractions import gcd
import sys
import os
parentdir = os.path.abspath('../..')
sys.path.append(parentdir)
from projecteuler.prime import rad
from projecteuler.p124 import p124

def solve(limit):
	count = 0
	csum = 0

	rlist = radlist(limit)
	sortedlist = sorted(rlist, key=lambda x: x[1])
	r = lambda x: rlist[x - 1][1]
	num = lambda x: rlist[x - 1][0]

	print rlist[:100]

	for c in range(3, limit + 1):
		# print c
		radc = r(c)
		for pair in sortedlist:
			a = pair[0]
			rada = pair[1]
			b = c - a
			if a >= b:
				continue

			radprod = radc*rada
			if radprod > c/2:
				break

			if gcd(a, b) == 1 and radprod*r(b) < c:
				count += 1
				csum += c
				print a, b, c

	return count, csum

def radlist(limit):
	numlist = list()
	for i in range(1, limit + 1):
		numlist.append((i, rad(i)))
	return numlist

if __name__ == '__main__':

	ans = 0
	if len(sys.argv) < 2:
		ans = solve(120000 - 1)
	else:
		ans = solve(int(sys.argv[1]))

	print "Answer = ", ans