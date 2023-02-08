import sys
sys.stdin = open("input.txt")

for _ in range(10) :
	t = int(input())
	graph = list()
	starts = list()
	first_row = list(map(int, input().split()))
	for j in range(100) :
		if first_row[j] == 1 :
			starts.append((0, j))
	graph.append(first_row)
	graph += [list(map(int, input().split())) for _ in range(99)]
	# 바닥까지 내려가는건 똑같으니 왼쪽 or 오른쪽을 움직이는 횟수만 비교
	cnt_min = 200
	answer = 100
	# 이전에 아래로 갔으면 0, 왼쪽으로 갔으면 1, 오른쪽으로 갔으면 2
	status = 0
	for start in starts :
		cnt_now = 0
		x, y = start
		while x < 100 :
			# 왼쪽으로
			if y > 0 and graph[x][y-1] and status in (0, 1) :
				y -= 1
				cnt_now += 1
				status = 1
				continue
			# 오른쪽으로
			elif y < 99 and graph[x][y+1] and status in (0, 2):
				y += 1
				cnt_now += 1
				status = 2
				continue
			# 아래로
			else :
				x += 1
				status = 0
		if cnt_min > cnt_now :
			cnt_min = cnt_now
			answer = start[1]
	print(f"#{t} {answer}")

