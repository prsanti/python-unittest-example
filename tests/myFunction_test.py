import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import src
from src.myFunction import Sum 

class SumTest(unittest.TestCase):
    def test_Sum(self):
        self.assertEqual(src.myFunction.Sum(1, 1), 2)
        self.assertTrue(src.myFunction.Sum(1, 2) == 3)