import sys
sys.stdin = open("input.txt")

for t in range(1, int(input())+1) :
	n = int(input())
	bus = [0] * 1001
	min_start = 1001
	max_end = 0
	for _ in range(n) :
		type, a, b = map(int, input().split())
		if min_start > a :
			min_start = a
		if max_end < b :
			max_end = b
		if type == 1 :
			bus[b] += 1
			for i in range(a, b) :
				bus[i] += 1
		elif type == 2 :
			bus[b] += 1
			for i in range(a, b, 2) :
				bus[i] += 1
		elif type == 3 :
			bus[b] += 1
			if a % 2 == 0 :
				if a % 4 == 0 :
					for i in range(a, b, 4) :
						bus[i] += 1
				elif a % 4 == 2 :
					bus[a] += 1
					for i in range(a+2, b, 4) :
						bus[i] += 1
			else :
				if a % 3 == 0 :
					start = a
				elif a % 3 == 1 :
					start = a + 2
				elif a % 3 == 2 :
					start = a + 1
				for i in range(start, b, 3) :
					if i % 10 == 0 :
						continue
					else :
						bus[i] += 1
	answer = 0
	for j in range(min_start, max_end+1) :
		if answer < bus[j] :
			answer = bus[j]
	print(f"#{t}", answer)