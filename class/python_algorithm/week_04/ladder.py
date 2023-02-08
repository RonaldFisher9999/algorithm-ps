import sys
sys.stdin = open("input.txt")

for _ in range(1, 4) :
	t = int(input())
	graph = [list(map(int, input().split())) for _ in range(99)]
	last_row = list(map(int, input().split()))
	graph.append(last_row)
	# 마지막 행에 있는 시작점 체크
	x, y = 99, 0
	for j in range(100) :
		if last_row[j] == 2 :
			y = j
	while x >= 0 :
		# 방문한 지점 체크
		graph[x][y] = 0
		# 왼쪽으로 갈 수 있으면 왼쪽으로
		if y > 0 and graph[x][y-1] == 1 :
			y -= 1
			continue
		# 오른쪽으로 갈 수 있으면 오른쪽으로
		elif y < 99 and graph[x][y+1] == 1 :
			y += 1
			continue
		# 어느 것도 아니면 위로
		else :
			x -= 1
	answer = y
	print(f"#{t} {answer}")


