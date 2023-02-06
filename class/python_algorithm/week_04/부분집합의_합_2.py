import sys
sys.stdin = open("input.txt")

arr = list(range(1, 13))
for t in range(1, int(input())+1) :
	n, k = map(int, input().split())
	answer = 0
	for sub_set in range(1, 1 << 12) :
		now_sum = 0
		cnt = 0
		for i in range(12) :
			if sub_set & (1 << i) :
				now_sum += arr[i]
				cnt += 1
			if cnt > n :
				break
		if now_sum == k and cnt == n :
			answer += 1
	print(f"#{t} {answer}")