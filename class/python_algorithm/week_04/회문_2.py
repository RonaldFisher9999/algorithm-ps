import sys
sys.stdin = open("input.txt")

def check(string) :
	n = len(string)
	for i in range(n // 2) :
		if string[i] != string[n-1-i] :
			return False
	return True

for t in range(1, 11) :
	m = int(input())
	arr = [list(input()) for _ in range(8)]
	answer = 0
	for row in arr :
		for j in range(9 - m) :
			string = row[j:j+m]
			if check(string) :
				answer += 1
	arr = list(zip(*arr))
	for row in arr :
		for j in range(9 - m) :
			string = row[j:j+m]
			if check(string) :
				answer += 1
	print(f"#{t} {answer}")

