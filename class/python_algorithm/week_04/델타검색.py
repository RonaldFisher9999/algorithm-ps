import sys
sys.stdin = open("input.txt")

def abs(num) :
	if num < 0 :
		num = -num
	return num

for t in range(1, int(input())+1) :
	n = int(input())
	graph = [list(map(int, input().split())) for _ in range(n)]
	move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
	answer = 0
	for x in range(n) :
		for y in range(n) :
			for dx, dy in move :
				nx = x + dx
				ny = y + dy
				if 0 <= nx < n and 0 <= ny < n :
					answer += abs((graph[nx][ny] - graph[x][y]))
	print(f"#{t}", answer)
