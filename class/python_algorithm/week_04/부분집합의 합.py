import sys
sys.stdin = open("input.txt")

for t in range(1, int(input())+1) :
	arr = list(map(int, input().split()))
	answer = 0
	for i in range(1, 1 << 10) :
		now_sum = 0
		for j in range(10) :
			if i & (1 << j) :
				now_sum += arr[j]
		if now_sum == 0 :
			answer += 1
			break
	print(f"#{t}", answer)