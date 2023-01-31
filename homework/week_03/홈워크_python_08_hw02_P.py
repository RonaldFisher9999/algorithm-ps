class Stack :
    def __init__(self) :
        self.array = list()

    def empty(self) :
        if self.array :
            return True
        else :
            return False

    def top(self) :
        if self.array :
            return self.array[-1]
        else :
            return None
    
    def pop(self) :
        if self.array :
            return self.array.pop()
        else :
            return None

    def push(self, value) :
        self.array.append(value)

    def __repr__(self) :
        print(self.array)

s1 = Stack()
print(s1.empty())
s1.push(5)
s1.push(4)
print(s1.pop())
print(s1.top())
s1.push(7)
s1.push(0)
s1.__repr__()
print(s1.empty())
