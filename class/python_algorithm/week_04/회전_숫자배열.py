import sys
sys.stdin = open("input.txt")

for t in range(1, int(input())+1) :
	n = int(input())
	arr = [list(input().split()) for _ in range(n)]
	print(f"#{t}")
	for i in range(n) :
		rot_90 = list()
		rot_180 = list()
		rot_270 = list()
		for j in range(n) :
			rot_90.append(arr[n-1-j][i])
			rot_180.append(arr[n-1-i][n-1-j])
			rot_270.append(arr[j][n-1-i])
		print("".join(rot_90), "".join(rot_180), "".join(rot_270))