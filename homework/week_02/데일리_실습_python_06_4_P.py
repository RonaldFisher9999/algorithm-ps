entry_record = ['이싸피', '박장고', '조실습', '이싸피', '조실습', '오디비', '임온실', '조실습', '조실습', '이싸피', '안도둑', '임온실', '최이썬', '오디비', '안도둑', '염자바', '박장고', '조실습',
                '최이썬', '조실습', '염자바', '박장고', '임온실', '임온실', '이싸피', '임온실', '오디비', '조실습', '염자바', '임온실', '박장고', '최이썬', '안도둑', '염자바', '임온실', '박장고', '이싸피', '안도둑',
                '임온실', '오디비', '최이썬', '안도둑', '이싸피', '오디비', '안도둑', '이싸피', '박장고', '박장고', '안도둑', '안도둑', '안도둑', '염자바', '최이썬', '오디비', '오디비', '최이썬', '이싸피', '임온실', '안도둑']

exit_record = ['최이썬', '조실습', '이싸피', '안도둑', '임온실', '안도둑', '이싸피', '오디비', '염자바', '박장고', '최이썬', '이싸피', '염자바', '염자바', '박장고', '임온실', '이싸피',
               '박장고', '안도둑', '염자바', '이싸피', '조실습', '조실습', '임온실', '박장고', '이싸피', '조실습', '박장고', '오디비', '안도둑', '조실습', '임온실', '안도둑', '안도둑', '임온실', '조실습', '최이썬', '안도둑', '임온실',
               '염자바', '이싸피', '임온실', '안도둑', '오디비', '안도둑', '오디비', '임온실', '염자바', '임온실', '박장고', '조실습', '이싸피', '최이썬', '최이썬', '오디비', '오디비', '염자바', '오디비', '안도둑', '박장고']

from collections import Counter

def max_entry(entry_record) :
    cnt = Counter(entry_record)
    return cnt.most_common(3)

def diff_record(entry_record, exit_record) :
    en_cnt = Counter(entry_record)
    ex_cnt = Counter(exit_record)
    more_en = dict()
    more_ex = dict()
    for person in en_cnt :
        if person not in ex_cnt :
            more_en[person] = en_cnt[person]
        else :
            diff = en_cnt[person] - ex_cnt[person]
            if diff > 0 :
                more_en[person] = diff
            elif diff < 0 :
                more_ex[person] = -diff
    for person in ex_cnt :
        if person not in en_cnt :
            more_ex[person] = ex_cnt[person]
    return more_en, more_ex

record_1 = max_entry(entry_record)
print("입장 기록이 많은 Top3")
for rec in record_1 :
    print(f"{rec[0]} {rec[1]}회")
print()

more_entry, more_exit = diff_record(entry_record, exit_record)
print("출입 기록이 수상한 사람")
for person in more_entry :
    print(f"{person}은 입장 기록이 {more_entry[person]}회 더 많아 수상합니다.")
for person in more_exit :
    print(f"{person}은 퇴장 기록이 {more_exit[person]}회 더 많아 수상합니다.")

