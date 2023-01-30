def collatz(n) :
    cnt = 0
    while n != 1 :
        if cnt == 500 :
            return -1
        if n % 2 == 0 :
            n = n // 2
            cnt += 1
            continue
        else :
            n = (n * 3) + 1
            cnt += 1
    return cnt

print(collatz(6))  # => 8
print(collatz(16))  # => 4
print(collatz(27))  # => 111
print(collatz(626331))  # => -1
