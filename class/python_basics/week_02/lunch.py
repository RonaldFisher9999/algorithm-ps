import random
class Lunch() :
    def __init__(self, all_stu, now_stu) :
        self.all_stu = ['고영진','구본웅','김성용','김하늘','김하림',
                        '김현아','민경현','배이경','서동훈','송준우',
                        '심현재','유창재','윤민영','윤태영','이민호',
                        '이성섭','이성우','이영아','이예슬','임수형',
                        '임혜진','정선재','정현아','진익근','최태호',
                        '최홍준','하정호','허주혁']
        students_set = set()
        file = None
        try :
            students_set = set(open("students_set.txt", "r").read().split())
        except :
            file = open("students_set.txt", "w")
            for s in self.all_stu :
                file.write(f"{s} ")
            file.close()
            students_set = set(open("students_set.txt", "r").read().split())
        self.now_stu = students_set