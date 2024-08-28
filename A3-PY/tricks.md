# Python is dynamically typed, Python is interpreted ,Python follows indenta1on and makes the code neat and readable

# Python is dynamically typed because in a code we need not

specify the type of variables while declaring them. The type of a
variable is not known un1l the code is executed

# When we say python is an interpreted language it means that

python code is not compiled before execu1on

# What is "**init**" ?

In Python, **init** is a special method used to initialize objects of a class. It's called a constructor method because it gets called when you create a new instance of the class , The transla1on of code to machine
language occurs while the program is being executed

# what is the usage of **name**?

In Python, the **name** attribute is a special variable that is automatically set in a script or module.
-> When the Python interpreter runs a script, it sets the **name** attribute of that script to "**main**". However,
-> if the script is imported as a module into another script, the **name** attribute is set to the name of the module
instead of "**main**".
This allows you to determine whether a script is being run as the main program or being imported as a module. It's commonly used to include code that should only run when the script is run directly, but not when it's imported.

How do methods and functions differ?
What does the "self" parameter in Python mean?

OOP follows four pillars:

Polymorphism – Ability of an object to take many forms
Inheritance – Child classes acquire properties from parent classes
Encapsulation – Protects data and methods from outside misuse by binding them together
Abstraction – Handles complexity by hiding unnecessary details from the user.

# The def keyword is used to create, (or deﬁne) a func1on in python

# Draw a comparison between the range and xrange in Python

# xrange() vs range()

x = xrange(1, 10)
y = range(1, 10)

print "Type(x) = ", type(x)
print "Type(y) = ", type(y)

Normally, xrange() is only used when the user wants his/her code to be only designed for Python 2.x versions as it is not available for Python 3.x versions. For Python 3 the range() method replaces the xrange() method instead.

The major difference between the two function is that, both of them return different objects with different properties.

# The xrange() method returns a xrange object which is an immutable sequence and which only supports iteration, indexing and len function as mentioned earlier.

# On the other hand, the range() method returns a list which supports major functions like slicing, pop() etc.

Moreover, xrange objects are more useful when we need to build code with minimal space complexity as it takes fairly constant memory size independent of the range of values it stores.

If you want to write a program that can be run or executed on both Python 2 and 3, using the range() method makes more sense and hence is recommended.

# What is a Decorator ?

Decorator is a function that provides a wrapper around another function. This way you can add additional functionality to an already existing code.​

A decorator is a design pattern in Python through which a user can add additional functionality to an existing object without modifying its underlying structure. Decorators are called before the definition of a function you want to decorate.​

So simplistically we can say decorators are functions which modify the functionality of other functions. They make the code more concise and pythonic. ​

# This is the decorated function​

@decorator_function​
def function_one():​
{​
print(“This function needs ​
to be decorated”)​
}​

# This is the decorator function​

def decorator_function(func):​
{​
print(“This is the decorator function”)​

      print(“This function does some decoration”)​

      return func;​

}​

# Client code​

      function_one()​

# What is an Iterator ?

Iterator in Python is simply an object that can be iterated upon, meaning you can traverse through all the values​

Technically, in Python , an iterator is an object which implements the iterator protocol, which consists of the methods **iter** and **next**​

Iterators are present everywhere in Python. They are elegantly implemented within for loops, comprehensions, generators etc. but it is hidden in plain sight

# What happens if you call the iter() function​

When we call the iter() function on an object, iter function first looks for an **iter**() method of that object​
If the **iter**() method exists, then iter() function calls **iter**() to get an iterator. Otherwise, the iter() function will look for a **getitem**() method​

If the **getitem**() is present, the iter() function creates an iterator object and returns that object. Otherwise, it raises a TypeError exception​

When both **iter**() and **getitem**() methods exist, the iter() function always uses the **iter**() method:

# What is an iterable

An object is called iterable if we can get an iterator from it. Most built-in containers in Python like list, tuple, set, dictionary and string are iterables​

If you pass an iterable to an iter() function, it returns an iterator. (iter() function in turn calls the**iter**() method)​

The process of traversing the iterable is called as iteration​

# What is an iterable, iterator and iter protocol ​

newlist = ["apple","orange","pineaple"]
newit = iter(newlist)
print(next(newit)) # apple
print(next(newit)) # orange
print(next(newit)) # pineaple

here newlist is the iterable​
newit is the iterator​
iter and next functions form the iter protocol​​

​
