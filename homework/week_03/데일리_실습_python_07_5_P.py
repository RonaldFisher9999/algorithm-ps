import random

class ClassHelper :
    def __init__(self, students) :
        self.students = students

    def pick(self, n) :
        return random.sample(self.students, n)

    def match_pair(self) :
        random.shuffle(self.students)
        pairs = []
        n = len(self.students)
        for i in range(0, n-1, 2) :
            pairs.append([self.students[i], self.students[i+1]])
        if n % 2 == 1 :
            pairs[-1].append(self.students[-1])
        return pairs


ch = ClassHelper(['김해피', '이해킹', '조민지', '박영수', '정민수'])

print(ch.pick(1))
print(ch.pick(1))
print(ch.pick(2))
print(ch.pick(3))
print(ch.pick(4))

print(ch.match_pair())
