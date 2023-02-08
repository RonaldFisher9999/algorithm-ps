import sys
sys.stdin = open("input.txt")

for t in range(1, int(input())+1) :
	str1 = input()
	str2 = input()
	answer = 0
	if str1 in str2 :
		answer = 1
	print(f"#{t} {answer}")