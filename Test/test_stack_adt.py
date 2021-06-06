from main import stack_adt
import pytest


def test_is_empty():
    x = stack_adt.ArrayStack()
    assert x.is_empty() == True

def test_push():
    x = stack_adt.ArrayStack()
    x.push(3)
    assert x.pop() == 3