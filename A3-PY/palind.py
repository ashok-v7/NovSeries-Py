def is_palindrome_number(num):
    return str(num) == str(num)[::-1]


def is_palindrome_string(num2):
    return s == num2[::-1]


# Example usage:
num1 = 121
num2 = "radar"

print(f"{num1} is palindrome: {is_palindrome_number(num1)}")
print(f"{num2} is palindrome: {is_palindrome_number(num2)}")
