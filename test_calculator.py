import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add1(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    def test_add2(self):
        self.assertEqual(self.calc.add(2, 2), 4)

    def test_substract1(self):
        self.assertEqual(self.calc.subtract(2, 1), 1)

    def test_substract2(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)

    def test_multiply1(self):
        self.assertEqual(self.calc.multiply(2, 2), 4)

    def test_multiply2(self):
        self.assertEqual(self.calc.multiply(3, 2), 6)

    def test_divide1(self):
        self.assertEqual(self.calc.divide(2, 2), 1)

    def test_divide2(self):
        self.assertEqual(self.calc.divide(4, 2), 2)

    def test_modulo1(self):
        self.assertEqual(self.calc.modulo(3, 2), 1)

    def test_modulo2(self):
        self.assertEqual(self.calc.modulo(5, 2), 1)

if __name__ == '__main__':
    unittest.main()