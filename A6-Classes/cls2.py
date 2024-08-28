class Computer:

    def __init__(self, cpu, ram):
        # cpu , ram are arguments in above and now add it to object
        self.cpu = cpu
        self.ram = ram
        print("in init")

    def config(self):
        print("i5 machine 16 GB")
        print("config is :", self.cpu, self.ram)


# object creation and passing values com1, i5 and 16GB as parameters and accepting in __init__
com1 = Computer("i5", "16 GB")
com2 = Computer("i7", "32GB")
com1.config()
com2.config()
