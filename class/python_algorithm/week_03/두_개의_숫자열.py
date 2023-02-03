import sys
sys.stdin = open("input.txt")

for t in range(1, int(input())+1) :
	# m이 더 크게
	n, m = map(int, input().split())
	if n > m :
		n, m = m, n
		arr_m = list(map(int, input().split()))
		arr_n = list(map(int, input().split()))
	else :
		arr_n = list(map(int, input().split()))
		arr_m = list(map(int, input().split()))
	answer = 0
	for i in range(m - n + 1) :
		now = 0
		for j in range(i, i + n) :
			now += arr_n[j-i] * arr_m[j]
		# print(f"now: {now}")
		if answer < now :
			answer = now
	print(f"#{t} {answer}")

