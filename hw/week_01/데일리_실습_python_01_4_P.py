sol = 0
n = 1000
for i in range(n + 1) :
    if i % 2 == 0 :
        sol += i
    elif i % 7 == 0 :
        sol += i
print(sol)
