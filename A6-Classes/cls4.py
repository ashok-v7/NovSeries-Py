class Car:

    # class variables
    wheels = 4

    def __init__(self):

        # Instance variables -- which are different for different objects , if we change one object it will not effect other object
        self.mileage = 10
        self.company = "Volvo"


c1 = Car()
c2 = Car()

c1.mileage = 20

print(c1.mileage, c1.wheels)
print(c2.mileage, c2.wheels)

Car.wheels = 5

print(c1.mileage, c1.wheels)
print(c2.mileage, c2.wheels)

'''
Instance variable vs Class(static) variable
'''
