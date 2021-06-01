import pytest
import unittest
import q2
import sys

def pytest():
    #pytest test
    assert q2.again(4) == True
    assert q2.again(100) == False
    assert q2.again(400) == False
    
print("----------PYTEST----------")
pytest()
print("----------END TEST--------")