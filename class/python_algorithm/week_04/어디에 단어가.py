import sys
sys.stdin = open("input.txt")

for t in range(1, int(input())+1) :
	n, k = map(int, input().split())
	graph = [list(map(int, input().split())) for _ in range(n)]
	answer = 0
	# 가로 방향
	for i in range(n) :
		for j in range(n - k + 1) :
			# 1 나오면 탐색 시작
			if graph[i][j] == 1 :
				# 연속한 1 중 처음이 아니면 탐색 중단
				if j >= 1 and graph[i][j-1] == 1 :
					continue
				# j를 고정하고 연속된 1의 개수 세줌
				x = j + 1
				cnt = 1
				while True :
					# 범위를 벗어나거나 0이 나오면 중단
					if x >= n or graph[i][x] == 0 :
						break
					# 1의 개수가 k를 넘으면 중단
					if cnt > k :
						break
					# 인덱스와 1의 개수 하나씩 추가
					else :
						x += 1
						cnt += 1
				# k와 일치하면 answer +1
				if cnt == k :
					answer += 1
	# 세로 방향
	for j in range(n) :
		for i in range(n - k + 1) :
			if graph[i][j] ==  1 :
				if i >= 1 and graph[i-1][j] == 1 :
					continue
				# i를 고정하고 1의 개수 세줌
				x = i + 1
				cnt = 1
				while True :
					if x >= n or graph[x][j] == 0 :
						break
					if cnt > k :
						break
					else :
						x += 1
						cnt += 1
				if cnt == k :
					answer += 1
	print(f"#{t}", answer)
