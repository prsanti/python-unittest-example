import unittest
from unittest import mock
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import src 
from src.myFunction import Random 

class RandomTest(unittest.TestCase):
    @mock.patch('os.urandom')
    def test_Random(self, random_mock):
        random_mock.return_value = 'aaa'
        self.assertEqual(src.myFunction.Random(2), '2aaa')