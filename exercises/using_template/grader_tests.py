import random
import unittest

from graderutils.graderunittest import points

import submission


def model_times_two(x):
    return x * 2


class TestExamplePython(unittest.TestCase):

    @points(5)
    def test_times_small(self):
        for i in range(10):
            self.assertEqual(submission.times_two(i), model_times_two(i),
                             "Multiplication was incorrect for small numbers.")

    @points(10)
    def test_times_large(self):
        for _ in range(100):
            param = random.randint(500, 1000000)
            self.assertEqual(submission.times_two(param), model_times_two(param),
                             "Multiplication was incorrect for large random numbers.")

    @points(15)
    def test_times_negative(self):
        for _ in range(100):
            param = random.randint(-1000000, -1)
            self.assertEqual(submission.times_two(param), model_times_two(param),
                             "Multiplication was incorrect for negative numbers.")
