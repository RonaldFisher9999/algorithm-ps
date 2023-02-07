import sys
sys.stdin = open("input.txt")

def bin_search(arr, n, d) :
	start = 0
	end = n - 1
	while start <= end :
		mid = (start + end) // 2
		if arr[mid] == d :
			return mid+1
		if arr[mid] < d :
			start = mid + 1
			continue
		if arr[mid] > d :
			end = mid - 1
			continue
	return 0

for t in range(1, int(input())+1) :
	n, d = map(int, input().split())
	arr = sorted(map(int, input().split()))
	answer = bin_search(arr, n , d)
	print(f"#{t} {answer}")