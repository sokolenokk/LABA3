import unittest
from task2 import Counter


class TestCounter(unittest.TestCase):
    def test_initial_value(self):
        counter = Counter(5)
        self.assertEqual(counter.get_value(), 5)

    def test_increment_plus_step(self):
        counter = Counter(10)
        counter.increment(3)
        self.assertEqual(counter.get_value(), 13)

    def test_increment_minus_step(self):
        counter = Counter(5)
        with self.assertRaises(ValueError):
            counter.increment(-3)

    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            Counter("число")


if __name__ == "__main__":
    unittest.main(verbosity=2)
