from InputDataValidator import InputDataValidator


class AbstractCalculator:
    def add(self, first, second):
        pass

    def divide(self, first, second):
        pass

    def derivative(self, function, order):
        pass


class Calculator(AbstractCalculator):
    def __init__(self):
        self._validator = InputDataValidator()

    def add(self, first, second):
        self._validator.validate(first, second, "SUM")
        return first+second

    def derivative(self, function, order):
        self._validator.validate(function, order, "DERIVATIVE")


calculator = Calculator()
calculator.derivative("3x+2", 1)
