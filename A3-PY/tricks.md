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
