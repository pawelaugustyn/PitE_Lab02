from InputDataValidator import InputDataValidator
import abc
import sympy
from math import log


class AbstractCalculator(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def add(self, first, second):
        """Adding two numbers"""

    @abc.abstractmethod
    def divide(self, first, second):
        """Divide first number by second"""

    @abc.abstractmethod
    def logarithm(self, number, base):
        """Logarithm of number 'number' counted on base 'base'"""

    @abc.abstractmethod
    def derivative(self, function, degree):
        """Function's degree's derivative"""


class Calculator(AbstractCalculator):
    def __init__(self):
        self._validator = InputDataValidator()

    def add(self, first, second):
        self._validator.validate(first, second, "SUM")
        return first+second

    def divide(self, first, second):
        self._validator.validate(first, second, "DIVISION")
        return first/second

    def logarithm(self, number, base):
        self._validator.validate(number, base, "LOGARITHM")
        return log(number, base)

    def derivative(self, function, degree):
        self._validator.validate(function, degree, "DERIVATIVE")
        return sympy.diff(function, 'x', degree)
