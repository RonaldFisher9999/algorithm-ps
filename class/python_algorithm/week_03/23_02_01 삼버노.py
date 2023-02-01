import sys
sys.stdin = open("input.txt")

t_num = int(input())
for t in range(1, t_num+1) :
	n = int(input())
	answer = [0] * 5001
	for _ in range(n) :
		a, b = map(int, input().split())
		for i in range(a, b+1) :
			answer[i] += 1
	print(f"#{t}", end=" ")
	for _ in range(int(input())) :
		print(answer[int(input())], end=" ")