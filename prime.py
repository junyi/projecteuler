import sys
import math

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

class Factors:
	def __init__(self, n):
		self.n = n
		self.factors = dict()

	def insert(self, k):
		if k in self.factors.keys():
			self.factors[k] += 1
		else:
			self.factors[k] = 1

def factorize(n):
	fact = Factors(n)

	while n > 1:
		is_prime = True
		for i in myxrange(2, int(math.sqrt(n)) + 1):
			# print i, n
			if n % i == 0:
				n /= i
				fact.insert(i)
				is_prime = False
				break
		if is_prime:
			fact.insert(n)
			n = 1

	return fact

def rad(n):
	factors = factorize(n).factors
	product = 1
	for i in factors.keys():
		product *= i
	return product 

def myxrange(a1, a2=None, step=1):
    if a2 is None:
        start, last = 0, a1
    else:
        start, last = a1, a2
    while cmp(start, last) == cmp(0, step):
        yield start
        start += step


def is_prime(n):
	for i in range(2, int(math.sqrt(n)) + 1):
		if n % i == 0:
			return True
	return False

if __name__ == '__main__':
	ans = 0
	if len(sys.argv) < 2:
		ans = factorize(27).factors
	else:
		ans = factorize(int(sys.argv[1])).factors

	print "Factors = ", ans
