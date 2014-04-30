import sys
import math

def solve():
	count = 0
	for i in range(1, 10):
		max_n = int(1//(1 - math.log(i, 10)))
		for n in range(1, max_n + 1):
			if len(str(pow(i, n))) == n:
				count += 1
	return count


if __name__ == '__main__':
	ans = solve()

	print "Count = ", ans
