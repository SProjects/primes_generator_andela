import unittest
from primes_generator import primes_generator


class TestPrimesGenerator(unittest.TestCase):

    def test_primes_generator_function_receives_an_argument(self):
        primes_generator(5)

    def test_primes_generator_raises_value_error_for_non_integer_argument(self):
        self.assertRaises(ValueError, primes_generator, [1, 2])
        self.assertRaises(ValueError, primes_generator, 'string')