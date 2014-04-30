import sys

def solve(limit):
	cf = [1] + [2] * limit
	i = 2
	f0 = (1, 1)
	f1 = (3, 2)
	count = 0

	while i < 1000:
		f = fraction(cf[i], f1, f0)
		f1, f0 = f, f1
		i += 1
		if len(str(f[0])) > len(str(f[1])):
			count += 1

	return count


def fraction(cf0, f1, f2):
	return (cf0*f1[0] + f2[0], cf0*f1[1] + f2[1])




# def binary_solve(f, start, end, limit, cur):
# 	mid = (start + end)/2.0

# 	if f(mid) == 0 or cur > limit:
# 		return mid

# 	if sign(f(start)) != sign(f(mid)):
# 		return binary_solve(f, start, mid, limit, cur + 1)
# 	elif sign(f(end)) != sign(f(mid)):
# 		return binary_solve(f, mid, end, limit, cur + 1)

# def sign(x):
# 	if x == 0.0:
# 		return 0
# 	elif x > 0.0:
# 		return 1
# 	else:
# 		return -1

if __name__ == '__main__':
	ans = 0
	if len(sys.argv) < 2:
		ans = solve(1000)
	else:
		ans = solve(int(sys.argv[1]))

	print "Count: ", ans