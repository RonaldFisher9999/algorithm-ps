import sys
sys.stdin = open("input.txt")

def bubble_sort(arr, n) :
	end = n - 1
	while True :
		if end == 0 :
			return arr
		for i in range(end) :
			if arr[i] > arr[i+1] :
				arr[i], arr[i+1] = arr[i+1], arr[i]
		end -= 1

t_num = int(input())
for t in range(1, t_num+1) :
	n = int(input())
	arr = list(map(int, input().split()))
	print(f"#{t}", end=" ")
	print(*bubble_sort(arr, n))