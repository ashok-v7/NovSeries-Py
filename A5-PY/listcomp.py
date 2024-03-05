# list comprehension
# x = [i for i in range(10)]
# print(x)

# x = [[j for j in range(5)]for i in range(10)]
# print(x)

x = [i for i in range(10) if i % 2 == 0]
print(x)

''''
List comprehension is a concise way to create lists in Python by applying an expression to each item in an iterable.
The star (*) method in list comprehension allows you to unpack elements of nested iterables, such as lists of tuples or lists of lists.
It flattens the nested structure and includes each element in the resulting list.

'''
