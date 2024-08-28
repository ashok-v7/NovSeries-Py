class Computer:
    # attribute and behaviour
    def config(self):
        print("i5 machine 16 GB")


# a = 5
# print(type(a))  # inbuilt class int
com1 = Computer()
com2 = Computer()
print(type(com1))  # our own computer class
# Everything is object in python
Computer.config(com1)  # self is the object we are passing
Computer.config(com2)
com1.config()  # behind the scene config will take com1 as argument
com2.config()

a = 5
a.bit_length


#######################
