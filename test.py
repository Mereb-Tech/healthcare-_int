import unittest
from calc import calculator

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculator(1, 2, 'add'), 3)
        self.assertEqual(calculator(-1, 1, 'add'), 0)
        self.assertEqual(calculator(-1, -1, 'add'), -2)

    def test_subtraction(self):
        self.assertEqual(calculator(2, 1, 'subtract'), 1)
        self.assertEqual(calculator(-1, -1, 'subtract'), 0)
        self.assertEqual(calculator(-1, 1, 'subtract'), -2)

    def test_multiplication(self):
        self.assertEqual(calculator(2, 3, 'multiply'), 6)
        self.assertEqual(calculator(-1, 1, 'multiply'), -1)
        self.assertEqual(calculator(-1, -1, 'multiply'), 1)

    def test_division(self):
        self.assertEqual(calculator(6, 3, 'divide'), 2)
        self.assertEqual(calculator(-6, -3, 'divide'), 2)
        self.assertEqual(calculator(-6, 3, 'divide'), -2)
        self.assertEqual(calculator(6, -3, 'divide'), -2)
        self.assertEqual(calculator(5, 2, 'divide'), 2.5)

    def test_division_by_zero(self):
        self.assertEqual(calculator(1, 0, 'divide'), "Error: Division by zero!")

    def test_invalid_operation(self):
        self.assertEqual(calculator(1, 1, 'modulo'), "Error: Invalid operation!")

if __name__ == '__main__':
    unittest.main()
