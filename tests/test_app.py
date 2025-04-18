import sys
import os
import pytest

# for some reason, it is needed with a current project structure
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import add, subtract, multiply


def test_add():
  assert add(2, 3) == 5
  assert add(-1, 1) == 0
  assert add(0, 0) == 0

def test_subtract():
  assert subtract(5, 3) == 2
  assert subtract(0, 5) == -5
  assert subtract(-3, -2) == -1

def test_multiply():
  assert multiply(2, 3) == 6
  assert multiply(-1, 5) == -5
  assert multiply(0, 10) == 0
