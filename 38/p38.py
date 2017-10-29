import sys
import os
parentdir = os.path.abspath('../..')
sys.path.append(parentdir)
import math
from collections import Counter
from itertools import permutations

pandigital = Counter('123456789')

def to_num(tuple):
	return int(''.join(str(i) for i in tuple))

def check_pandigital(num, n):
	lst = []
	for i in xrange(1, n + 1):
		lst.append(str(num * i))

	s = ''.join(lst)
	return Counter(s) == pandigital, s

def solve():
	limits = {}
	for n in xrange(2, 10):
		c = int(math.ceil(9. / n))
		maximum = int((10 ** c - 1) / n)
		minimum = int(10 ** (c - 2))
		limits[n] = (minimum, maximum)

	pandigital_set = set()

	for n, (minimum, maximum) in limits.iteritems():
		print n, minimum, maximum
		for num in xrange(minimum, maximum + 1):
			s = str(num)
			if '0' in s or set(Counter(s).values()) != set([1]):
				continue
			result, value = check_pandigital(num, n)
			if result:
				pandigital_set.add(value)

	return max(pandigital_set)

if __name__ == '__main__':
	ans = solve()
	print "Answer = ", ans
