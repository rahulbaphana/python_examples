import unittest
from my_math import Operations

class CheckNumbers(unittest.TestCase):
    def test_int_float(self):
        self.assertEqual(1, 1.0)

    def test_str_float(self):
        self.assertEqual(str(1), "1")

    def test_should_add_two_parameters(self):
        self.assertEqual(Operations().add(1,2), 3)
        self.assertEqual(Operations().add("Hello","World!"), "HelloWorld!")       