class Student:
    school = "NCC"

    def __init__(self, m1, m2, m3):
        # instance varaibles
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        # this is an instance method as we are passing self it means it belongs to a particular object
        # accessor method , mutator method
        # fetch -- accessor method , modify -- mutator method
        return (self.m1 + self.m2 + self.m3)/3

    def get_m1(self):
        return self.m1

    def set_m1(self, value):
        self.m1 = value

    def info(cls):
        # if we are working instance -- use self
        # if we are working with class -- use cls
        return cls.school


s1 = Student(30, 60, 90)
s2 = Student(50, 40, 50)
print(s1.avg())
print(s2.avg())
print(s1.m1)
print(Student.info())

'''
instance methods
class methods
static methods
class methods and static methods are different
'''
