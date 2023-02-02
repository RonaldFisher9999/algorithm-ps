import sys
sys.stdin = open("input.txt")

for t in range(1, int(input())+1) :
	n = int(input())
	# 마지막 값이 1일 경우에도 최대값 갱신하기 위해 0 추가
	arr = input() + "0"
	# 최대 연속한 1의 개수
	max_cnt = 0
	# 현재 연속한 1의 개수
	now_cnt = 0
	for i in range(n+1) :
		# 1이면 count 시작
		if arr[i] == "1" :
			now_cnt += 1
			continue
		# count 중이었는데 0이 나온 경우 count 중단
		if now_cnt != 0 and arr[i] == "0" :
			# 최대값 갱신
			if max_cnt < now_cnt :
				max_cnt = now_cnt
			# 현재값 초기화
			now_cnt = 0
	print(f"#{t} {max_cnt}")
