# Iterable class
class MyIterable:
    def __init__(self):
        self.data = [1, 2, 3]

    def __iter__(self):
        return iter(self.data)


# Using the iterable
my_iterable = MyIterable()
for item in my_iterable:
    print(item)
