import pytest
import unittest
import q2
import sys

def pytest():
    #pytest test
    assert q2.again(4) == True
    
print("----------PYTEST----------")
pytest()
print("----------END TEST--------")