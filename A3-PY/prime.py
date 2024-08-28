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


# A prime number is a positive number  with only two factors  : itself and 1
# A perfect number A perfect number is a positive integer equal to the total of its positive divisors,
# except the number itself in number theory. For example, 6 is a perfect number since 1 + 2 + 3 equals 6.
# A composite number is a positive number with more than two factors  -- 21 --> 1,3,7,21


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


# Perfect number
# 4 - 4 % (1,2,3)
n = int(input("Enter any number: "))
sum1 = 0
for i in range(1, n):
    if (n % i == 0):
        sum1 = sum1 + i
if (sum1 == n):
    # 6 -- 1 + 2 + 3
    print("The number is a Perfect number!")
else:
    print("The number is not a Perfect number!")


# Composite number
def is_composite(number):
    ''' We start by checking if the number is less than 4, as numbers less than 4 are neither prime nor composite.
If the number is greater than or equal to 4, we iterate from 2 to the number and check if it is divisible by any number other than 1 and itself.
If we find such a divisor, we return True, indicating that the number is composite.
Otherwise, we return False.
    '''
    if number < 4:
        return False
    for i in range(2, number):
        if number % i == 0:
            return True
    return False


# User input
num = int(input("Enter a number: "))

if is_composite(num):
    print(num, "is a composite number.")
else:
    print(num, "is not a composite number.")
