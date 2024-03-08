
from Mul import mul


def func1():
    mul()  # to resuse add import stmt
    print("from fun1")


def func2():
    print("from fun2")


def main():
    print("from main")
    func1()
    func2()


main()
