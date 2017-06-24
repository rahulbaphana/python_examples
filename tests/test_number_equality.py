import unittest
from my_math import Operations
import sys

sys.dont_write_bytecode = True

class CheckNumbers(unittest.TestCase):
    def should_test_int_float(self):
        self.assertEqual(1, 1.0)

    def should_test_str_float(self):
        self.assertEqual(str(1), "1")

    def should_test_add_two_parameters(self):
        self.assertEqual(Operations().add(1,2), 3)
        # self.assertEqual(Operations().add("Hello","World!"), "HelloWorld!")       