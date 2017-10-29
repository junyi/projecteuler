import sys
import os
parentdir = os.path.abspath('../..')
sys.path.append(parentdir)

def cycle_length(n, dividend=10):
	remainders = []
	remainder = -1
	count = 0
	while remainder != 0:
		remainder = dividend % n
		remainders.append(remainder)
		try:
			index = remainders.index(remainder)
			if count > index:
				return count - index
		except ValueError:
			pass
		dividend = 10 * remainder
		count += 1
	return 0

def powers_2_or_5(n):
	while n > 1:
		if n % 2 == 0:
			n /= 2
		elif n % 5 == 0:
			n /= 5
		else:
			return False
	return True

def solve(limit=1000):
	num = 0
	max_length = 0
	for i in xrange(1000):
		if not powers_2_or_5(i):
			length = cycle_length(i)
			if length > max_length:
				max_length = length
				num = i
	return num

if __name__ == '__main__':
	ans = solve()
	print "Answer = ", ans
