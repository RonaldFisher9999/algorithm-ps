import sys
sys.stdin = open("input.txt")

# def min(x, y) :
# 	if x <= y :
# 		return x
# 	return y
#
# def max(x, y) :
# 	if x >= y :
# 		return x
# 	return y
#
# def color_area(xy_1_lu, xy_1_rd, xy_2_lu, xy_2_rd) :
# 	cnt = 0
# 	for i in range(max(xy_1_lu[0], xy_2_lu[0]), min(xy_1_rd[0], xy_2_rd[0]) + 1) :
# 		for j in range(max(xy_1_lu[1], xy_2_lu[1]), min(xy_1_rd[1], xy_2_rd[1]) + 1) :
# 			if not colored[i][j] :
# 				colored[i][j] = 1
# 				cnt += 1
# 	return cnt
#
# for t in range(1, int(input())+1) :
# 	n = int(input())
# 	colored = [[0] * 10 for _ in range(10)]
# 	papers = list()
# 	for _ in range(n) :
# 		r1, c1, r2, c2, color = map(int, input().split())
# 		papers.append(((r1, c1), (r2, c2), color))
# 	answer = 0
# 	for i in range(n-1) :
# 		for j in range(i+1, n) :
# 			# 두 종이의 색이 다르면 겹치는 넓이 계산
# 			if papers[i][2] != papers[j][2] :
# 				area = color_area(papers[i][0], papers[i][1], papers[j][0], papers[j][1])
# 				answer += area
# 	print(f"#{t} {answer}")

for t in range(1, int(input())+1) :
	n = int(input())
	colored = [[0] * 10 for _ in range(10)]
	answer = 0
	for _ in range(n) :
		r1, c1, r2, c2, color = map(int, input().split())
		for i in range(r1, r2+1) :
			for j in range(c1, c2+1) :
				colored[i][j] += color
				if colored[i][j] == 3 :
					answer += 1
	print(f"#{t} {answer}")

# for t in range(1, int(input())+1) :
# 	n = int(input())
# 	answer = 0
# 	red = set()
# 	blue = set()
# 	for _ in range(n) :
# 		r1, c1, r2, c2, color = map(int, input().split())
# 		if color == 1 :
# 			for i in range(r1, r2+1) :
# 				for j in range(c1, c2+1) :
# 					red.add((i, j))
# 					if (i, j) in blue :
# 						answer += 1
# 		else :
# 			for i in range(r1, r2+1) :
# 				for j in range(c1, c2+1) :
# 					blue.add((i, j))
# 					if (i, j) in red :
# 						answer += 1
# 	print(f"#{t} {answer}")