# 입력 예시
class Point :
    def __init__(self, x, y) :
        self.x = x
        self.y = y

class Rectangle :
    def __init__(self, p1, p2) :
        self.left_up = p1
        self.right_down = p2
        self.width = self.right_down.x - self.left_up.x
        self.length = self.left_up.y - self.right_down.y

    def get_area(self) :   
        return self.width * self.length

    def get_perimeter(self) :
        return (self.width + self.length) * 2

    def is_square(self) :
        if self.width == self.length :
            return True
        else :
            return False

p1 = Point(1, 3)
p2 = Point(3, 1)
r1 = Rectangle(p1, p2)
print(r1.get_area())
print(r1.get_perimeter())
print(r1.is_square())

p3 = Point(3, 7)
p4 = Point(6, 4)
r2 = Rectangle(p3, p4)
print(r2.get_area())
print(r2.get_perimeter())
print(r2.is_square())

# 출력 예시
# 4
# 8
# True

# 9
# 12
# True