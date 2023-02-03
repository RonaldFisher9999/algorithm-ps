import sys

sys.stdin = open("input.txt")

for t in range(1, int(input()) + 1) :
	n, q = map(int, input().split())
	arr = [0] * n
	for x in range(1, q + 1) :
		l, r = map(int, input().split())
		for i in range(l - 1, r) :
			arr[i] = x
	print(f"#{t}", *arr)

