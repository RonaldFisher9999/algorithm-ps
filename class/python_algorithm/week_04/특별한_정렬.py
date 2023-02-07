import sys
sys.stdin = open("input.txt")

for t in range(1, int(input())+1) :
	n = int(input())
	arr = list(map(int, input().split()))
	answer = [0] * n
	for start in range(n - 1) :
		max_idx = start
		for i in range(start + 1, n) :
			if arr[max_idx] < arr[i] :
				max_idx = i
		arr[max_idx], arr[start] = arr[start], arr[max_idx]
	for i in range(n // 2) :
		answer[i*2] = arr[i]
	for j in range(n // 2) :
		answer[j*2+1] = arr[n-1-j]
	if n % 2 == 1 :
		answer[-1] = arr[n//2]
	print(f"#{t}", *answer[:10])

