class Computer:
    def __init__(self):
        self.name = "avn"
        self.age = 55

    def update(self):
        self.age = 55

    def compare(self, other):  # first c1, second c2 argument
        if self.age == other.age:
            return True
        else:
            return False


c1 = Computer()
c2 = Computer()

print(c1.name)
print(c2.name)

c1.name = "raj"
c1.age = 30
c1.update()  # it will pass c1 to update method in self
print(c1.name, c1.age)
print(c2.name, c2.age)

if c1.compare(c2):
    print("They are asame ")
else:
    print("They are are not same ")


'''
size of an object depends on no of variable
who allocates size to object -- constructor 
Whenver we write a constructor it will call init method for you
'''
