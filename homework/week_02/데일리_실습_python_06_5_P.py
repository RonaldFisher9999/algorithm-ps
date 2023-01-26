# 반복문 활용
def sum_of_digit_1(num) :
    num = str(num)
    answer = 0
    for s in num :
        answer += int(s)
    return answer

# 반복문 활용 X
def sum_fo_digit_2(num) :
    return sum(map(int, list(str(num))))

nums = [34, 1435, 3904]

for num in nums :
    print(sum_of_digit_1(num), sum_fo_digit_2(num))