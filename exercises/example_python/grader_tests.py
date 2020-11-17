import random
import string
import unittest

from graderutils.graderunittest import points

import submission


def model_greeting(x):
    return "Hello, " + x + "!"


def generate_random_string(length):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))


class TestExamplePython(unittest.TestCase):

    @points(5)
    def test_greeting_small(self):
        for _ in range(10):
            param = generate_random_string(5)
            self.assertEqual(submission.greeting(param), model_greeting(param),
                             "Greeting was incorrect for short arguments.")


    @points(10)
    def test_greeting_large(self):
        for _ in range(100):
            p_len = random.randint(6, 10)
            param = generate_random_string(p_len)
            self.assertEqual(submission.greeting(param), model_greeting(param),
                             "Greeting was incorrect for long arguments.")


    @points(15)
    def test_greeting_extra_large(self):
        for _ in range(100):
            p_len = random.randint(11, 15)
            param = generate_random_string(p_len)
            self.assertEqual(submission.greeting(param), model_greeting(param),
                             "Greeting was incorrect for very long arguments.")
