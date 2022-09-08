import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        # result = (10 + 5)
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(2, 5), 7)
        self.assertEqual(calc.add(3, 2), 5)

    def test_subract(self):
        # result = (10 + 5)
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(2, 5), -3)
        self.assertEqual(calc.subtract(3, 2), 1)

    def test_multiply(self):
        # result = (10 + 5)
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(2, 5), 10)
        self.assertEqual(calc.multiply(3, 1), 3)

    def test_divide(self):
        # result = (10 + 5)
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(6, 2), 3)
        self.assertEqual(calc.divide(3, 1), 3)

        with self.assertRaises(ValueError):
            calc.divide(10, 0)

if __name__ == "__main__" :
    unittest.main() 
