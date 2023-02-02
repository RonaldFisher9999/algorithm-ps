import sys
sys.stdin = open("s_input.txt")

t_num = int(input())
for t in range(1, t_num+1) :
	n = int(input())
	arr = list(map(int, input().split()))
	answer = 0
	for i in range(n) :
		if arr[i] :
			cnt = 0
			for j in range(i+1, n) :
				if arr[i] <= arr[j] :
					cnt += 1
			answer = max(answer, n-1 - i - cnt)
	print(f"#{t} {answer}")


