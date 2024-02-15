import math
def find_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def find_palindrome(n):
    return str(n) == str(n)[::-1]
def problem_1(max):
    return sum(i for i in range(max) if i % 3 == 0 or i % 5 == 0)
def problem_2(max):
    a, b = 1, 2
    total = 0
    while a <= max:
        if a % 2 == 0:
            total += a
        a, b = b, a + b
    return total
def problem_3(num):
    x = 0
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0 and find_prime(i):
            x = i
    return x
def problem_4():
    max = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            palindrome = i * j
            if find_palindrome(palindrome) and palindrome > max:
                max = palindrome
    return max
def problem_5(max):
    result = 1
    for i in range(2, max + 1):
        result *= i // math.gcd(i, result)
    return result
