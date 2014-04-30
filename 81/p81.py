import sys

def solve(path_to_file):
	matrix = list()
	result_matrix = list()
	with open(path_to_file, 'r') as f:
		for line in f:
			matrix.append([int(i) for i in line.split(',')])
			result_matrix.append([-1] * len(matrix[-1]))

	current_row = 0
	current_col = 0

	queue = list()
	queue.append((matrix[0][0], (0,0)))
	result_matrix[0][0] = matrix[0][0]

	width = len(matrix[0])
	height = len(matrix)
	dimen = (width, height)

	while queue:
		pos = queue.pop(0)[1]
		print pos
		queue = solve_matrix(matrix, result_matrix, queue, pos, dimen)

	# print result_matrix
	return result_matrix[height - 1][width - 1]

def solve_matrix(matrix, result_matrix, queue, pos, dimen):
	row = pos[0]
	col = pos[1]
	width = dimen[0]
	height = dimen[1]

	is_row_at_end = row == height - 1
	is_col_at_end = col == width - 1

	if is_row_at_end and is_col_at_end:
		return sorted(queue)

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

	return sorted(queue)


if __name__ == '__main__':
	ans = 0
	if len(sys.argv) < 2:
		ans = solve('matrix.txt')
	else:
		ans = solve(sys.argv[1])

	print "Shortest path sum = ", ans
