"""Small math and text utilities."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("cannot divide by zero")
    return a / b


def power(base, exp):
    return base ** exp


def is_even(n):
    return n % 2 == 0


def factorial(n):
    if n < 0:
        raise ValueError("n must be >= 0")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def fibonacci(n):
    """Return the first n Fibonacci numbers as a list."""
    if n < 0:
        raise ValueError("n must be >= 0")
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_palindrome(text):
    cleaned = "".join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]


def word_count(text):
    return len(text.split())


def reverse_words(text):
    return " ".join(reversed(text.split()))


def celsius_to_fahrenheit(c):
    return round(c * 9 / 5 + 32, 2)


def average(numbers):
    if not numbers:
        return 0
    return round(sum(numbers) / len(numbers), 2)
