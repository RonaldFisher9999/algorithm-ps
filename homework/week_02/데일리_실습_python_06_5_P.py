# 반복문 활용
def sum_of_digit_1(num) :
    num = str(num)
    answer = 0
    for s in num :
        answer += int(s)
    return answer

# 반복문 활용 X
def sum_of_digit_2(num) :
    return sum(map(int, list(str(num))))

# 재귀 활용
def sum_of_digit_3(num) :
    if num < 10 :
        return num
    return num % 10 + sum_of_digit_3(num // 10)

nums = [34, 1435, 3904]

for num in nums :
    print(sum_of_digit_1(num))
    print(sum_of_digit_2(num))
    print(sum_of_digit_3(num))