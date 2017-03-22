# PitE_Lab02

https://travis-ci.org/pawelaugustyn/PitE_Lab02.svg?branch=master

Files in that folder realise second home assignment from Python in the Enterprise's labs.

File Calculator.py
- simple calculator which provides four mathematical operations: add, divide, log and derivative.
- built on interface AbstractCalculator
- handles exceptions when given wrong datatype

File InputDataValidator.py
- class which gives an ability to check input data


File testingcalculator.py
- unit tests for calculator's features
- run every time commited, thanks to travis

File exceptions.py
- all additional exception to give a feedback


Usage:
import Calculator

AVailable operations:
Calculator.add(first, second) - add first number to second
Calculator.divide(first, second) - divide first number with second
Calculator.logarithm(number, base) - count a logarithm of a number with specified base
Calculator.derivative(function, multiplicity) - count multiplicitied derivative of specified function
