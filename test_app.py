import pytest

from app import (
    add, average, celsius_to_fahrenheit, divide, factorial, fibonacci,
    is_even, is_palindrome, is_prime, multiply, power, reverse_words,
    subtract, word_count,
)


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 3) == 2


def test_multiply():
    assert multiply(4, 3) == 12


def test_divide():
    assert divide(10, 4) == 2.5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)


def test_power():
    assert power(2, 5) == 32


def test_is_even():
    assert is_even(4)
    assert not is_even(7)


def test_factorial():
    assert factorial(0) == 1
    assert factorial(5) == 120


def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-1)


def test_fibonacci():
    assert fibonacci(7) == [0, 1, 1, 2, 3, 5, 8]
    assert fibonacci(0) == []


def test_is_prime():
    assert is_prime(2)
    assert is_prime(13)
    assert not is_prime(1)
    assert not is_prime(15)


def test_is_palindrome():
    assert is_palindrome("A man, a plan, a canal: Panama")
    assert not is_palindrome("hello")


def test_word_count():
    assert word_count("the quick brown fox") == 4
    assert word_count("") == 0


def test_reverse_words():
    assert reverse_words("one two three") == "three two one"


def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212


def test_average():
    assert average([10, 20, 30]) == 20
    assert average([]) == 0
