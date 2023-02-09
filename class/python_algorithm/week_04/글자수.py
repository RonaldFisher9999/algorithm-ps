import sys
sys.stdin = open("input.txt")

for t in range(1, int(input())+1) :
	str1 = input()
	str2 = input()
	cnt_dict = {s : 0 for s in str1}
	for s in str2 :
		if s in cnt_dict :
			cnt_dict[s] += 1
	answer = 0
	for cnt in cnt_dict.values() :
		if answer < cnt :
			answer = cnt
	print(f"#{t} {answer}")