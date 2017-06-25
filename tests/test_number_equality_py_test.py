import unittest

class TestMathOperations(unittest.TestCase):
    def test_equality_of_int_with_float(self):
        assert 1 == 1.0

    def test_int_str(self):
        assert 1 == 1