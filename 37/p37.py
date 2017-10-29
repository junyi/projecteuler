import sys
import os
parentdir = os.path.abspath('../..')
sys.path.append(parentdir)
from projecteuler import prime

def truncatable_prime(num):
	primes = set()
	for i in xrange(1, len(str(num))):
		primes.add(int(str(num)[i:]))
		primes.add(int(str(num)[:i]))

	if '1' in primes:
		return False

	return all(prime.is_prime(i) for i in primes)

def solve():
	MAX = 11
	total = 0
	num = 13
	while True:
		if prime.is_prime(num) and truncatable_prime(num):
			print num
			total += num
			MAX -= 1
			if MAX == 0:
				break

		num += 2

	return total

if __name__ == '__main__':
	ans = solve()
	print "Answer = ", ans
