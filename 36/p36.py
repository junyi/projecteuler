import sys
import os
parentdir = os.path.abspath('../..')
sys.path.append(parentdir)
from math import ceil

def palindrome(s):
	l = len(s)
	return all([s[i] == s[l - i - 1] for i in xrange(int(ceil(l / 2.)))])

def palindrome210(num):
	return palindrome(str(num)) and palindrome(bin(num)[2:])

def solve():
	MAX = 10 ** 6
	total = 0
	for num in xrange(1, MAX):
		if palindrome210(num):
			total += num

	return total

if __name__ == '__main__':
	ans = solve()
	print "Answer = ", ans
