import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition_with_integers(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_addition_with_floats(self):
        self.assertAlmostEqual(self.calc.add(2.5, 1.2), 3.7, places=7)
        self.assertAlmostEqual(self.calc.add(-1.1, -2.2), -3.3, places=7)

    def test_addition_with_large_numbers(self):
        self.assertEqual(self.calc.add(10**12, 10**12), 2 * 10**12)

    def test_subtraction_with_integers(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        self.assertEqual(self.calc.subtract(0, 5), -5)

    def test_subtraction_with_floats(self):
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.2), 3.3, places=7)
        self.assertAlmostEqual(self.calc.subtract(-1.5, 1.5), -3.0, places=7)

    def test_multiplication_with_integers(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-2, 5), -10)
        self.assertEqual(self.calc.multiply(0, 100), 0)

    def test_multiplication_with_floats(self):
        self.assertAlmostEqual(self.calc.multiply(2.5, 2), 5.0, places=7)
        self.assertAlmostEqual(self.calc.multiply(-1.5, -2), 3.0, places=7)

    def test_multiplication_with_large_numbers(self):
        self.assertEqual(self.calc.multiply(10**6, 10**3), 10**9)

    def test_division_normal(self):
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5, places=7)
        self.assertAlmostEqual(self.calc.divide(-9, 3), -3.0, places=7)

    def test_division_with_floats(self):
        self.assertAlmostEqual(self.calc.divide(2.5, 0.5), 5.0, places=7)
        self.assertAlmostEqual(self.calc.divide(-1.5, 0.5), -3.0, places=7)

    def test_divide_by_zero_returns_none(self):
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(0, 0))

    def test_division_edge_cases(self):
        # division that results in a repeating float
        result = self.calc.divide(1, 3)
        self.assertIsInstance(result, float)
        self.assertAlmostEqual(result, 1.0 / 3.0, places=7)

    def test_operations_with_mixed_types(self):
        self.assertAlmostEqual(self.calc.add(1, 2.5), 3.5, places=7)
        self.assertAlmostEqual(self.calc.multiply(3, 2.5), 7.5, places=7)
        self.assertAlmostEqual(self.calc.subtract(5.5, 2), 3.5, places=7)
        self.assertAlmostEqual(self.calc.divide(5, 2.0), 2.5, places=7)

if __name__ == "__main__":
    unittest.main()
