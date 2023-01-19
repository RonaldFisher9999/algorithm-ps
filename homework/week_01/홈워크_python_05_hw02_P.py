# fn_d(91) 
# 출력 예시 
# 101

n = int(input())

def fn_d(n) :
    sol = n + sum(map(int, str(n)))
    return sol

print(f"{n} generates {fn_d(n)}")

m = int(input())

def is_selfnumber(m) :
    check = [0] * (2 * m)
    for i in range(1, m + 1) :
        check[fn_d(i)] = 1
    if check[m] == 0 :
        return True
    else :
        return False

print(f"Is {m} self-number? {is_selfnumber(m)}")