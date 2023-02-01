import sys
sys.stdin = open("input.txt")

t_num = int(input())
for t in range(1, t_num+1) :
	num = int(input())
	prime_dict = {p : 0 for p in (2, 3, 5, 7, 11)}
	for p in prime_dict :
		while num % p == 0 :
			num = num // p
			prime_dict[p] += 1
	print(f"#{t}", end=" ")
	print(*prime_dict.values())