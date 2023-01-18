# 입력 예시
# 2015
# 8
# 31

# 출력 예시 
#경고 월요일입니다.
#{'년': 2015, '월': 8, '일': 31, '요일': '월요일'}

import calendar

year = int(input("연도 입력 : "))

while calendar.isleap(year) :
    print(f"{year}년은 윤년입니다.")
    year = int(input("연도 재입력 : "))
calendar.prcal(year)

month = int(input("월 입력 : "))
day = int(input("일 입력 : "))

week = {0:'월요일', 1:'화요일', 2:'수요일', 3:'목요일', 4:'금요일', 5:'토요일', 6:'일요일'}
weekday = week[calendar.weekday(year, month, day)]

if weekday == '월요일' :
    print("경고 월요일입니다.")
output = {'년' : year, '월' : month, '일' : day, '요일' : weekday}
print(output)

