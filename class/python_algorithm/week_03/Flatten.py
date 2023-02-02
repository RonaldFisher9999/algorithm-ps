import sys
sys.stdin = open("input.txt")

# def counting_sort(arr, n) :
# 	cnt_arr = [0] * (n+1)
# 	for num in arr :
# 		cnt_arr[num] += 1
# 	for i in range(1, n+1) :
# 		cnt_arr[i] += cnt_arr[i-1]
# 	result = [0] * n
# 	for num in arr :
# 		result[cnt_arr[num]-1] = num
# 		cnt_arr[num] -= 1
# 	return result
#
# for t in range(1, 11) :
# 	total_dump = int(input())
# 	arr = list(map(int, input().split()))
# 	arr = counting_sort(arr, 100)
# 	diff = 100
# 	while total_dump :
# 		dump = 0
# 		dump_1 = arr[1] - arr[0]
# 		dump_2 = arr[-1] - arr[-2]
# 		if dump_1 == 0 or dump_2 == 0 :
# 			dump = 1
# 		elif dump_1 < dump_2 :
# 			dump = dump_1
# 		else :
# 			dump = dump_2
# 		if total_dump < dump :
# 			dump = total_dump
# 		arr[0] += dump
# 		arr[-1] -= dump
# 		arr = counting_sort(arr, 100)
# 		diff = arr[-1] - arr[0]
# 		if diff == 0 or diff == 1 :
# 			break
# 		else :
# 			total_dump -= dump
# 	print(f"#{t} {diff}")

def get_max(arr, n) :
	max_val = 0
	idx = 0
	for i in range(n) :
		if max_val < arr[i] :
			max_val = arr[i]
			idx = i
	return max_val, idx

def get_min(arr, n) :
	min_val = 101
	idx = 0
	for i in range(n) :
		if min_val > arr[i] :
			min_val = arr[i]
			idx = i
	return min_val, idx

for t in range(1, 11) :
	total_dump = int(input())
	arr = list(map(int, input().split()))
	diff = get_max(arr, 100)[0] - get_min(arr, 100)[0]
	while total_dump :
		if diff == 0 or diff == 1:
			break
		arr[get_max(arr, 100)[1]] -= 1
		arr[get_min(arr, 100)[1]] += 1
		total_dump -= 1
		diff = get_max(arr, 100)[0] - get_min(arr, 100)[0]
	print(f"#{t} {diff}")

