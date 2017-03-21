import exceptions
import abc


class AbstractValidator(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def validate(self, first, second, equation_type):
        """validate the input"""


class InputDataValidator(AbstractValidator):
    def validate(self, first, second, equation_type):
        if equation_type != "DERIVATIVE" and (not self._is_number(first) or not self._is_number(second)):
            raise exceptions.NotANumber
        if equation_type == "DERIVATIVE":
            if not self._is_string(first):
                raise exceptions.NotAFunction
            if not self._is_integer(second):
                raise exceptions.NotInteger
            if self._is_negative(second):
                raise exceptions.NotPositiveNumber
        if equation_type == "LOGARITHM":
            if not self._is_positive(second):
                raise exceptions.NotValidLogarithmBase
            if self._is_log_base_one(second):
                raise exceptions.NotValidLogarithmBase
            if not self._is_positive(first) or not self._is_positive(second):
                raise exceptions.NotPositiveNumber
        if equation_type == "DIVISION" and self._is_zero(second):
            raise exceptions.DividingByZero

    @staticmethod
    def _is_number(checked_number):
        if isinstance(checked_number, int):
            return True
        elif isinstance(checked_number, float):
            return True
        return False

    @staticmethod
    def _is_string(checked_object):
        return isinstance(checked_object, str)

    @staticmethod
    def _is_zero(checked_object):
        if checked_object < 10**-10:
            if checked_object > -1*10**-10:
                return True
        return False

    @staticmethod
    def _is_positive(checked_object):
        return checked_object > 0

    @staticmethod
    def _is_negative(checked_object):
        return checked_object < 0

    @staticmethod
    def _is_log_base_one(checked_object):
        return checked_object == 1

    @staticmethod
    def _is_integer(checked_object):
        return isinstance(checked_object, int)