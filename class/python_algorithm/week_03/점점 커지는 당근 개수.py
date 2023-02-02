import sys
sys.stdin = open("input.txt")

for t in range(1, int(input())+1) :
	n = int(input())
	arr = list(map(int, input().split())) + [0]
	max_cnt = 1
	now_cnt = 1
	for i in range(1, n+1) :
		if arr[i] > arr[i-1] :
			now_cnt += 1
			continue
		if now_cnt > 1 and arr[i] <= arr[i-1] :
			if max_cnt < now_cnt :
				max_cnt = now_cnt
				now_cnt = 1
	print(f"#{t} {max_cnt}")