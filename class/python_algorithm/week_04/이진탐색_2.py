import sys
sys.stdin = open("input.txt")

def bin_search(p, target) :
	start = 1
	end = p
	cnt = 1
	while start <= end :
		mid = (start + end) // 2
		if mid == target :
			break
		if mid < target :
			start = mid
			cnt += 1
			continue
		if mid > target :
			end = mid
			cnt += 1
	return cnt

for t in range(1, int(input())+1) :
	p, a, b = map(int, input().split())
	cnt_a = bin_search(p, a)
	cnt_b = bin_search(p, b)
	if cnt_a < cnt_b :
		print(f"#{t} A")
	elif cnt_a > cnt_b :
		print(f"#{t} B")
	else :
		print(f"#{t} 0")