import unittest
from unittest.mock import patch
from Calculator import Calculator
import exceptions


class TestCalculator(unittest.TestCase):
    ###########################
    # Testing add operation ###
    ###########################
    def test_adding_two_integers(self):
        c = Calculator()
        first = 23
        second = 345
        expected_result = 368
        self.assertEqual(expected_result, c.add(first, second))

    def test_adding_two_floats(self):
        c = Calculator()
        first = 23.3
        second = 12.3
        expected_result = 35.6
        self.assertAlmostEqual(expected_result, c.add(first, second))

    def test_adding_negative_values(self):
        c = Calculator()
        first = -3
        second = -7
        excepted_result = -10
        self.assertEqual(excepted_result, c.add(first, second))

    def test_adding_int_and_string_raises_exception(self):
        c = Calculator()
        first = 234
        second = "ala"
        self.assertRaises(exceptions.NotANumber, c.add, first, second)

    def test_adding_two_strings_raises_exception(self):
        c = Calculator()
        first = "string"
        second = "my_second_string"
        self.assertRaises(exceptions.NotANumber, c.add, first, second)

    ###############################
    # Testing divide operation  ###
    ###############################
    def test_dividing_two_ints(self):
        c = Calculator()
        first = 6
        second = 2
        expected_result = 3
        self.assertEqual(expected_result, c.divide(first, second))

    def test_dividing_int_with_float(self):
        c = Calculator()
        first = 5
        second = 2.5
        expected_result = 2
        self.assertAlmostEqual(expected_result, c.divide(first, second))

    def test_dividing_two_floats(self):
        c = Calculator()
        first = 6.4
        second = 1.6
        expected_result = 4
        self.assertAlmostEqual(expected_result, c.divide(first, second))

    def test_dividing_by_negative_value(self):
        c = Calculator()
        first = 6.4
        second = -1.6
        excepted_result = -4
        self.assertAlmostEqual(excepted_result, c.divide(first, second))

    def test_dividing_two_negative_values(self):
        c = Calculator()
        first = -6.4
        second = -3.2
        excepted_result = 2
        self.assertEqual(excepted_result, c.divide(first, second))

    def test_dividing_with_string_raises_exception(self):
        c = Calculator()
        first = 4
        second = "Liczba"
        self.assertRaises(exceptions.NotANumber, c.divide, first, second)

    def test_dividing_by_zero_raises_exception(self):
        c = Calculator()
        first = 5
        second = 0
        self.assertRaises(exceptions.DividingByZero, c.divide, first, second)

    ###################################
    # Testing logarithm operation   ###
    ###################################
    def test_logarithm_correct_result(self):
        c = Calculator()
        number = 8
        base = 2
        excepted_result = 3
        self.assertEqual(excepted_result, c.logarithm(number, base))

    def test_logarithm_by_one_raises_exception(self):
        c = Calculator()
        number = 8
        base = 1
        self.assertRaises(exceptions.NotValidLogarithmBase, c.logarithm, number, base)

    def test_logarithm_base_lower_than_zero_raises_exception(self):
        c = Calculator()
        number = 123
        base = -1
        self.assertRaises(exceptions.NotValidLogarithmBase, c.logarithm, number, base)

    def test_logarithm_number_lower_or_equals_zero_raises_exception(self):
        c = Calculator()
        number = -2
        base = 3
        self.assertRaises(exceptions.NotPositiveNumber, c.logarithm, number, base)

    def test_logarithm_base_equals_zero_raises_exception(self):
        c = Calculator()
        number = 234
        base = 0
        self.assertRaises(exceptions.NotValidLogarithmBase, c.logarithm, number, base)

    ###################################
    # Testing derivative operation  ###
    ###################################
    @patch('sympy.diff', return_value="sin(x)")
    def test_derivative_correct_answer(self, mock):
        c = Calculator()
        equation = "sin(x)"
        degree = 100
        excepted_result = "sin(x)"
        self.assertEqual(excepted_result, c.derivative(equation, degree))

if __name__ == "__main__":
    unittest.main()
