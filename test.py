import pytest
import unittest
import q1
import sys

def pytest():
    #pytest test
    assert q1.fizz_buzz(3) == 'Fizz'
    assert q1.fizz_buzz(5) == 'Buzz'
    assert q1.fizz_buzz(15) == 'FizzBuzz'
    assert q1.fizz_buzz(30) == 'FizzBuzz'
    assert q1.fizz_buzz(55) == 'Buzz'


print("----------PYTEST----------")
pytest()
print("----------END TEST--------")