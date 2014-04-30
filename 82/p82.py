import sys

def solve(path_to_file):
	matrix = list()
	with open(path_to_file, 'r') as f:
		for line in f:
			matrix.append([int(i) for i in line.split(',')])

	width = len(matrix[0])
	height = len(matrix)
	dimen = (width, height)	
	minlist = list()

	for row in range(height):
		print "Current row: ", row
		result_matrix = list()
		for i in range(height):
			result_matrix.append([-1]*width)

		queue = list()
		queue.append((matrix[row][0], (row,0)))
		result_matrix[row][0] = matrix[row][0]


		while queue:
			pos = queue.pop(0)[1]
			# print pos
			queue = solve_matrix(matrix, result_matrix, queue, pos, dimen)

		# print result_matrix
		cur_min = -1
		for i in range(height):
			if cur_min == -1 or result_matrix[i][width - 1] < cur_min:
				cur_min = result_matrix[i][width - 1]
		minlist.append(cur_min)

	return min(minlist)

def solve_matrix(matrix, result_matrix, queue, pos, dimen):
	row = pos[0]
	col = pos[1]
	width = dimen[0]
	height = dimen[1]

	is_row_at_end = row == height - 1
	is_col_at_end = col == width - 1
	is_row_at_top = row == 0

	cur = result_matrix[row][col]
	if not is_col_at_end:
		right = result_matrix[row][col + 1]
		temp = cur + matrix[row][col + 1]
		if right == -1:
			result_matrix[row][col + 1] = temp 
			queue.append((result_matrix[row][col + 1], (row, col + 1)))
		else:
			result_matrix[row][col + 1] = min(temp, right)

	if not is_row_at_end:
		down = result_matrix[row + 1][col]
		temp = cur + matrix[row + 1][col]
		if down == -1:
			result_matrix[row + 1][col] = temp
			queue.append((result_matrix[row + 1][col], (row + 1, col)))
		else:
			result_matrix[row + 1][col] = min(temp, down)

	if not is_row_at_top:
		up = result_matrix[row - 1][col]
		temp = cur + matrix[row - 1][col]
		if up == -1:
			result_matrix[row - 1][col] = temp
			queue.append((result_matrix[row - 1][col], (row - 1, col)))
		else:
			result_matrix[row - 1][col] = min(temp, up)

	return sorted(queue)


if __name__ == '__main__':
	ans = 0
	if len(sys.argv) < 2:
		ans = solve('matrix.txt')
	else:
		ans = solve(sys.argv[1])

	print "Shortest path sum = ", ans
