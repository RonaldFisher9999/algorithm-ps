import sys
sys.stdin = open("input.txt")

def check(word) :
	n = len(word)
	for i in range(n//2) :
		if word[i] != word[n-1-i] :
			return False
	return True

for t in range(1, int(input())+1) :
	n, m = map(int, input().split())
	arr = [list(input()) for _ in range(n)]
	answer = ""
	#가로
	for i in range(n) :
		for j in range(n - m + 1) :
			now = arr[i][j:j+m]
			if check(now) :
				answer = "".join(now)
				break
	# 세로
	if not answer :
		for j in range(n) :
			for i in range(n - m + 1) :
				now = [arr[x][j] for x in range(i, i+m)]
				if check(now) :
					answer = "".join(now)
					break
	print(f"#{t} {answer}")

