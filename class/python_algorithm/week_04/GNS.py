import sys
sys.stdin = open("input.txt")

for t in range(1, int(input()) + 1) :
	case, n = input().split()
	n = int(n)
	num_dict = {"ZRO" : 0, "ONE" : 1, "TWO" : 2, "THR" : 3, "FOR" : 4, "FIV" : 5, "SIX" : 6, "SVN" : 7, "EGT" : 8, "NIN" : 9}
	rev_dict = {b : a for a, b in num_dict.items()}
	nums = [0] * 10
	arr = input().split()
	for num in arr :
		nums[num_dict[num]] += 1
	answer = list()
	for i in range(10) :
		answer.extend([rev_dict[i]] * nums[i])
	print(f"#{t}")
	print(" ".join(answer))