import unittest
from primes_generator import primes_generator


class TestPrimesGenerator(unittest.TestCase):

    def test_primes_generator_function_receives_an_argument(self):
        primes_generator(5)

    def test_primes_generator_raises_value_error_for_non_integer_argument(self):
        self.assertRaises(ValueError, primes_generator, [1, 2])
        self.assertRaises(ValueError, primes_generator, 'string')

    def test_primes_generator_raises_value_error_for_argument_less_than_2(self):
        self.assertRaises(ValueError, primes_generator, -1)

    def test_primes_generator_returns_primes_up_to_the_limit_integer_argument(self):
        results = primes_generator(10)
        self.assertEqual(results, [2, 3, 5, 7])