# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True


# # Example usage
# number = 29
# if is_prime(number):
#     print(f"{number} is a prime number.")
# else:
#     print(f"{number} is not a prime number.")


# Python program to display all the prime numbers within an interval

lower = 8
upper = 11

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
    # all prime numbers are greater than 1
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
