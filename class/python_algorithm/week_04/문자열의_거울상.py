import sys
sys.stdin = open("input.txt")

for t in range(1, int(input())+1) :
	word = input()[::-1]
	answer = ""
	for s in word :
		if s == "b" :
			answer += "d"
		elif s == "d" :
			answer += "b"
		elif s == "p" :
			answer += "q"
		else :
			answer += "p"
	print(f"#{t} {answer}")