import sys
sys.stdin = open("input.txt")

for t in range(1, 4) :
	n = int(input())
	arr = list(map(int, input().split()))
	answer = 0
	for i in range(2, n-2) :
		next_max = 0
		for next in [-2, -1, 1, 2] :
			if next_max < arr[i+next] :
				next_max = arr[i+next]
		view = arr[i] - next_max
		if view < 0 :
			view = 0
		answer += view
	print(f"#{t} {answer}")