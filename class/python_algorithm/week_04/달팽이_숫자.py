import sys
sys.stdin = open("input.txt")

def snail(arr, n, start, x, y) :
	if n == 1 :
		arr[x][y] = start
		return
	else :
		for j in range(y, y+n-1) :
			arr[x][j] = start
			start += 1
		for i in range(x, x+n-1) :
			arr[i][y+n-1] = start
			start += 1
		for j in range(y+n-1, y, -1) :
			arr[x+n-1][j] = start
			start += 1
		for i in range(x+n-1, x, -1) :
			arr[i][y] = start
			start += 1
		if n == 2 :
			return
		snail(arr, n-2, start, x+1, y+1)

for t in range(1, int(input())+1) :
	n = int(input())
	arr = [[0] * n for _ in range(n)]
	snail(arr, n, 1, 0, 0)
	print(f"#{t}")
	for row in arr :
		print(*row)