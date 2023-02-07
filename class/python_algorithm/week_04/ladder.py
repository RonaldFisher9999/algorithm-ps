import sys
sys.stdin = open("input.txt")

def valid(x, y) :
	if 0 <= x < 100 and 0 <= y < 100 :
		return True
	return False

for _ in range(1, 4) :
	t = int(input())
	graph = list()
	for i in range(100) :
		row = list(map(int, input().split()))
		for j in range(100) :
			if row[j] == 2 :
				x, y = i, j
		graph.append(row)
	answer = -1
	graph[x][y] = 0
	while True :
		u_x, u_y = x - 1, y
		l_x, l_y = x, y - 1
		r_x, r_y = x, y + 1
		# 위쪽 범위 O and 길 O
		if valid(u_x, u_y) and graph[u_x][u_y] == 1 :
			# 왼쪽 범위 X or 길 X and 오른쪽 범위 X or 길 X -> 위쪽으로
			if (not valid(l_x, l_y) or graph[l_x][l_y] == 0) and (not valid(r_x, r_y) or graph[r_x][r_y] == 0) :
				graph[x][y] = 0
				x, y = u_x, u_y
				continue
			# 왼쪽 범위 O and 길 O -> 왼쪽으로
			if valid(l_x, l_y) and graph[l_x][l_y] == 1 :
				graph[x][y] = 0
				x, y = l_x, l_y
				continue
			# 오른쪽 범위 O and 길 O -> 오른쪽으로
			if valid(r_x, r_y) and graph[r_x][r_y] == 1 :
				graph[x][y] = 0
				x, y = r_x, r_y
				continue
		# 위쪽 범위 X or 길 X
		if not valid(u_x, u_y) or graph[u_x][u_y] == 0 :
			# 왼쪽 범위 X or 길 X and 오른쪽 범위 X or 길 X -> 제일 윗줄에 도착 = 출발점
			if (not valid(l_x, l_y) or graph[l_x][l_y] == 0) and (not valid(r_x, r_y) or graph[r_x][r_y] == 0) :
				answer = y
				break
			# 왼쪽 범위 O and 길 O -> 왼쪽으로
			if valid(l_x, l_y) and graph[l_x][l_y] == 1 :
				graph[x][y] = 0
				x, y = l_x, l_y
				continue
			# 오른쪽 범위 O and 길 O -> 오른쪽으로
			if valid(r_x, r_y) and graph[r_x][r_y] == 1 :
				graph[x][y] = 0
				x, y = r_x, r_y
				continue
	print(f"#{t} {answer}")