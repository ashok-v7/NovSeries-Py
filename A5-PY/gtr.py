'''
Generators are a special type of iterable that generate values lazily on-the-fly using the yield keyword.
Generators allow you to create iterators without the need to implement a full iterator class.
They are memory-efficient, especially when dealing with large datasets or infinite sequences
'''

# Generator function


def my_generator():
    yield 1
    yield 2
    yield 3


# Using the generator
gen = my_generator()
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3
