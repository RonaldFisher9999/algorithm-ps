import sys
sys.stdin = open("input.txt")

def check(a, b, i) :
	for j in range(m) :
		if b[j] != a[i+j] :
			return False
	return True

for t in range(1, int(input())+1) :
	a, b = input().split()
	n = len(a)
	m = len(b)
	i = 0
	answer = 0
	while i < n - m + 1 :
		if check(a, b, i) :
			i += m
		else :
			i += 1
		answer += 1
	answer += n - i
	print(f"#{t} {answer}")