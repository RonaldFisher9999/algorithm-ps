import sys
sys.stdin = open("input.txt")

t_num = int(input())
for t in range(1, t_num+1) :
	n, m = map(int, input().split())
	arr = list(map(int, input().split()))
	max_sum = 0
	min_sum = int(1e9)
	for i in range(n - m + 1) :
		now_sum = 0
		for j in range(i, i+m) :
			now_sum += arr[j]
		if max_sum < now_sum :
			max_sum = now_sum
		if min_sum > now_sum :
			min_sum = now_sum
	answer = max_sum - min_sum
	print(f"#{t} {answer}")