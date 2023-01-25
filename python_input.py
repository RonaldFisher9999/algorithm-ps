import sys
sys.stdin = open('input.txt')

# f = open("input.txt")
# input = f.readline

m, n = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
target = int(input())
cnt = 0
for i in range(n) :
    for j in range(m) :
        if array[i][j] == target :
            cnt += 1
print(m, n)
print(array)
print(target)
print(f"number of target in the array : {cnt}")