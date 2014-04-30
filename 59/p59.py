import sys

def solve(path_to_file):
	content = list()
	with open(path_to_file, 'r') as f:
		for line in f:
			content += [int(i) for i in line.split(',')]

	print len(content)

	for i in range(ord('g'), ord('z') + 1):
		for j in range(ord('o'), ord('z') + 1):
			for k in range(ord('d'), ord('z') + 1):
				key = (i, j, k)

				decrypted = list()
				x = 0
				while x < len(content):
					d = key[x % 3] ^ content[x]
					if d in range(256):
						decrypted.append(chr(d))
						x += 1
					else:
						continue

				joined = ''.join(decrypted)
				# print ''.join([chr(n) for n in key])
				# print joined

				if 'The Gospel of John' in joined:
					print ''.join([chr(n) for n in key])
					print joined
					print len(joined)
					sum = 0
					for i in joined:
						sum += ord(i)
					return sum


if __name__ == '__main__':
	ans = 0
	if len(sys.argv) < 2:
		ans = solve('cipher1.txt')
	else:
		ans = solve(sys.argv[1])

	print "Sum = ", ans
