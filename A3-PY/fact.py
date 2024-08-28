# def factorial(n):
#     if n < 0:
#         return "Factorial does not exist for negative numbers"
#     elif n == 0 or n == 1:
#         return 1
#     else:
#         fact = 1
#         for i in range(2, n + 1):
#             fact *= i
#         return fact


# # Example usage
# number = 5
# print(f"The factorial of {number} is {factorial(number)}.")


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


x = factorial(4)
print(x)
