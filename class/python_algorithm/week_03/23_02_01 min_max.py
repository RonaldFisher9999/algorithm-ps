import sys
sys.stdin = open("input.txt")

t_num = int(input())
for t in range(1, t_num+1) :
	n = int(input())
	arr = map(int, input().split())
	max_num = 0
	min_num = 1000000
	for num in arr :
		if max_num < num :
			max_num = num
		if min_num > num :
			min_num = num
	answer = max_num - min_num
	print(f"#{t} {answer}")