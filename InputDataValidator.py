class NotANumber(Exception):
    pass


class DividingByZero(Exception):
    pass


class NotAFunction(Exception):
    pass


class InputDataValidator:
    def validate(self, first, second, equation_type):
        if equation_type != "DERIVATIVE" and (not self._is_number(first) or not self._is_number(second)):
            raise NotANumber
        if equation_type == "DERIVATIVE" and (not self._is_function(first) or self._is_number(second)):
            raise NotAFunction
        if equation_type == "DIVISION" and second < 10**-4:
            raise DividingByZero

    @staticmethod
    def _is_number(checked_number):
        return isinstance(checked_number, int)

    @staticmethod
    def _is_function(checked_object):
        return isinstance(checked_object, str)