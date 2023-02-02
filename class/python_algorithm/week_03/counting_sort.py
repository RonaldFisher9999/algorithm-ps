import sys
sys.stdin = open("input.txt")

def counting_sort(arr) :
	cnt_arr = [0] * 101
	for num in arr :
		cnt_arr[num] += 1
	sorted_arr = list()
	for i in range(100) :
		if cnt_arr[i] :
			sorted_arr.extend([i] * cnt_arr[i])
	return sorted_arr

for t in range(1, int(input())+1) :
	n = int(input())
	arr = map(int, input().split())
	answer = counting_sort(arr)
	print(f"#{t}", end=" ")
	print(*answer)