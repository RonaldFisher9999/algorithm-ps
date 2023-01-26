import sys
sys.stdin = open('input.txt')

# f = open("input.txt")
# input = f.readline

n = int(input())
m = int(input())
edges = list()
for _ in range(m) :
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
edges.sort()

parent = list(range(n + 1))

def find_par(x) :
    if parent[x] != x :
        parent[x] = find_par(parent[x])
    return parent[x]

def union(a, b) :
    a = find_par(a)
    b = find_par(b)
    if a < b :
        parent[b] = a
    else :
        parent[a] = b

result = 0
for edge in edges :
    cost, a, b = edge
    if find_par(a) != find_par(b) :
        union(a, b)
        result += cost

print(result)