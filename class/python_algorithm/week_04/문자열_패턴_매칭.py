import sys
sys.stdin = open("input.txt", encoding='UTF-8')

for _ in range(10) :
	t = int(input())
	target = input().rstrip()
	m = len(target)
	string = input().rstrip()
	n = len(string)
	answer = 0
	for i in range(n - m + 1) :
		for j in range(m) :
			if target[j] != string[i+j] :
				break
		else :
			answer += 1
	print(f"#{t} {answer}")