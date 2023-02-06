import sys
sys.stdin = open("input.txt")

def max(iterable) :
	answer = iterable[0]
	for i in range(1, len(iterable)) :
		if answer < iterable[i] :
			answer = iterable[i]
	return answer

def sum(iterable) :
	answer = 0
	for i in range(len(iterable)) :
		answer += iterable[i]
	return answer

for _ in range(10) :
	t = int(input())
	arr = list()
	max_row, max_col, max_diag = 0, 0, 0
	col_sum = [0] * 100
	diag_1, diag_2 = 0, 0
	for i in range(100) :
		arr = list(map(int, input().split()))
		max_row = max([max_row, sum(arr)])
		for j in range(100) :
			col_sum[j] += arr[j]
		diag_1 += arr[i]
		diag_2 += arr[99 - i]
	max_col = max(col_sum)
	max_diag = max([diag_1, diag_2])
	answer = max([max_row, max_col, max_diag])
	print(f"#{t} {answer}")
