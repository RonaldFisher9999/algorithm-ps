import sys
sys.stdin = open("input.txt")

for t in range(1, int(input())+1) :
	n = int(input())
	arr = list(map(int, input()))
	cnt_arr = [0] * 10
	max_cnt = 0
	for num in arr :
		cnt_arr[num] += 1
		if max_cnt < cnt_arr[num] :
			max_cnt = cnt_arr[num]
	for i in range(9, -1, -1) :
		if cnt_arr[i] == max_cnt :
			print(f"#{t} {i} {max_cnt}")
			break
