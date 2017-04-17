import unittest
from primes_generator import primes_generator


class TestPrimesGenerator(unittest.TestCase):

    def test_primes_generator_function_receives_an_argument(self):
        primes_generator(5)