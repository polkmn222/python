# 생성자

class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second

a = FourCal()
a.setdata(4, 2)
print(a.first)
print(a.second)

a = FourCal()
b = FourCal()

a.setdata(4, 2)
print(a.first)

b.setdata(3, 7)
print(b.first)

print(id(a.first))
print(id(b.first))

class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

a = FourCal()
a.setdata(4, 2)
print(a.add())

class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def div(self):
        result = self.first / self.second
        return result

a = FourCal()
b = FourCal()
a.setdata(4, 2)
b.setdata(3, 8)

print(a.add())
print(a.sub())
print(a.mul())
print(a.div())

print(b.add())
print(b.sub())
print(b.mul())
print(b.div())

class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def div(self):
        result = self.first / self.second
        return result
    
a = FourCal(4, 2)
print(a.first)
print(a.second)

print(a.add())
print(a.sub())

# 클래스 상속

class MoreFourCal(FourCal):
    pass

a = MoreFourCal(4, 2)
print(a.add())
print(a.sub())
print(a.mul())
print(a.div())

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

a = MoreFourCal(4, 2)
print(a.pow())

class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

a = SafeFourCal(4, 0)
print(a.div())

