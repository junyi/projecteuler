import sys
import os
parentdir = os.path.abspath('../..')
sys.path.append(parentdir)
from projecteuler import prime

def solve(limit):
	numlist = list()
	for i in range(1, limit + 1):
		numlist.append((i, prime.rad(i)))

	sortedlist = sorted(numlist, key=lambda x: x[1])
	print len(sortedlist)
	return sortedlist

if __name__ == '__main__':

	ans = 0
	if len(sys.argv) < 2:
		ans = solve(100000)[9999]
	else:
		ans = solve(int(sys.argv[1]))[:100]

	print "Answer = ", ans