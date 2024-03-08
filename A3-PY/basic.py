
x = 5           # int
y = 3.14        # float
name = "Alice"  # str
is_active = True  # bool


a = 10
b = 3
print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication
print(a / b)  # Division
print(a % b)  # Modulus
print(a ** b)  # Exponentiation
print("// operator 10//3:", 10//3)


first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name  # String concatenation
print(full_name)
print("Hello " * 3)  # Repetition


if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")


for i in range(5):  # range(5) generates numbers from 0 to 4
    print(i)

# While Loop: Repeats as long as a condition is true.
count = 5
while count > 0:
    print(count)
    count -= 1


def greet(name):
    return "Hello, " + name


print(greet("Alice"))

#  list are  ordered , mutable collection
numbers = [5, 1, 7, 6, 10, 5]
print("numbers", numbers)
numbers.append(19)  # Add an element
print("numbers[0]", numbers[0])  # Access element
print("numbers.pop", numbers.pop(3))  # Remove at index
print("after pop-numbers", numbers)

person = {"name": "Alice", "age": 30}
person["age"] = 31  # Update value
print(person["name"])  # Access value


""" 
class: A blueprint for creating objects. Classes define a set of attributes and methods that their instances will have.

Object: An instance of a class. It is a concrete item in your program.

Inheritance: Allows a new class to extend an existing class. The new class inherits the properties and methods of the existing class.

Encapsulation: Hiding the internal state of an object and requiring all interaction to be performed through an object's methods.

Polymorphism: The ability to present the same interface for differing underlying forms (data types).

"""


class Dog:
    # Class Attribute
    species = "Canis familiaris"

    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"


buddy = Dog("Buddy", 9)
print(buddy.description())  # Buddy is 9 years old
print(buddy.speak("Woof Woof"))  # Buddy says Woof Woof


# inheritence
# Parent class
class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Woof!"

# Child class


class RussellTerrier(Dog):
    def run(self, speed):
        return f"{self.name} runs {speed}"

# Child class


class Bulldog(Dog):
    def sleep(self):
        return f"{self.name} sleeps a lot"


# encapsulation
class Computer:
    def __init__(self):
        self.__max_price = 900  # Private attribute

    def sell(self):
        return f"Selling Price: {self.__max_price}"

    def set_max_price(self, price):
        self.__max_price = price


c = Computer()
print(c.sell())  # Selling Price: 900

# change the price
c.set_max_price(1000)
print(c.sell())  # Selling Price: 1000


# polymorphism

class Dog:
    def speak(self):
        return "Woof!"


class Cat:
    def speak(self):
        return "Meow!"


animals = [Dog(), Cat()]

for animal in animals:
    print(animal.speak())


"""
Python program with a class Car that has two attributes: brand and speed. 
Add a method to increase the speed. Then, create two instances of Car and demonstrate changing their speeds.
"""


class Car:
    def __init__(self, brand, speed=0):
        self.brand = brand
        self.speed = speed

    def increase_speed(self, amount):
        self.speed += amount
        return f"The speed of the {self.brand} is now {self.speed} km/h."


# Creating two instances of Car
car1 = Car("Toyota")
car2 = Car("Ford", 30)

# Increase the speed of the cars
print(car1.increase_speed(20))  # Increases Toyota's speed by 20 km/h
print(car2.increase_speed(15))  # Increases Ford's speed by 15 km/h
