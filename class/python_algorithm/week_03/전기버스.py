import sys
sys.stdin = open("input.txt")

for t in range(1, int(input())+1) :
	k, n, m = map(int, input().split())
	stops = set(map(int, input().split()))
	now = n
	cnt = 0
	print(f"#{t}", end=" ")
	while True :
		# 현재 지점까지 올 수 있는 가장 먼 정류소 탐색
		for i in range(now - k, now) :
			# 출발점 도착하면 탐색 종료
			if i <= 0 :
				now = i
				break
			# 범위 내에 정류소가 있으면 그 정류소로 이동, cnt에 1 추가
			if i in stops :
				now = i
				cnt += 1
				break
		# 출발점에 도착하지도 못하고, 범위 내에 정류소도 없으면 현 지점 도착 불가
		else :
			print(0)
			break
		# 출발점에 도착했으므로 cnt 출력하고 종료
		if now <= 0 :
			print(cnt)
			break
