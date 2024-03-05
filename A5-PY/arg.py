# function arguments and parameter types

# def cmpfunc(x, y,z ):
#     print(x, y)
#     pass


# cmpfunc(1, 2,z=6)  #position and keyword arguments

# def cmpfunc(x, y, *args):
#     print(x, y, args)
#     pass


# cmpfunc(1, 2, 3, 4, 5, 6)


def cmpfunc(x, y, *args, **kwargs):
    print(x, y, args, kwargs)
    pass


cmpfunc(1, 5, 6, 7, 8, a=1, b=2)
