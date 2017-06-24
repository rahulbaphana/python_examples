import unittest

from my_math import Operations


class CheckNumbers(unittest.TestCase):
    
    def should_test_add_two_parameters(self):
        self.assertEqual(Operations().add(1,2), 3)

    def should_test_sum_of_numbers_list(self):
        self.assertEqual(Operations().iterative_sum([1,3,7]), 11)   

    def should_test_sum_of_numbers_list_tail_rec(self):     
        self.assertEqual(Operations().tail_rec_sum([1,3,7]), 11)    
