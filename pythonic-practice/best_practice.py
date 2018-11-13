#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This is the example module. This module does stuff.
"""
__author__ = ["[Davis Hong](https://github.com/davislf2)"]
__copyright__ = "Copyright 2018, The Boundary of Knowledge Project"
__credits__ = "Davis Hong"
__license__ = "MIT License"
__version__ = "0.1.0"
__maintainer__ = "Davis Hong"
__email__ = "davislf2.net@gmail.com"
__status__ = "Prototype"
__date__ = '13/11/2018'


import os
import sys
import collections
from os import chdir, chown
# from my_module import path

#  Imports should be grouped in the following order:
#     standard library imports
#     related third party imports
#     local application/library specific imports
# You should put a blank line between each group of imports.

# -------- Ch 1 - PEP 8 ------------------------
# Author
# Reference
# https://github.com/mikeckennedy/write-pythonic-code-demos

# ******** Part 1 - Imports **************************
import collections


#  Imports should be grouped in the following order:
#
#     standard library imports
#     related third party imports
#     local application/library specific imports
#
# You should put a blank line between each group of imports.

# ******** Part 2 - Code Layout **************************
class AClass:
    def m1(self):
        pass

    def m2(self):
        pass


def some_method(a1, a2):
    """
    some_method returns the larger num

    :param a1: num1
    :param a2: num2
    :return: 1 or 2
    """
    if a1 > a2:
        return 1
    elif a1 < a2:
        return 2
    else:
        return 0


def method2(a1):
    """
    This is good
    :param a1:
    :return:
    """
    sen = a1


print(some_method(0, 0.0))

text = "This is a string which is longer than 79 characters. This is not encouraged but will execute and run OK. Maybe."

# blank lines
# Surround top-level function and class definitions with two blank lines.
# Method definitions inside a class are surrounded by a single blank line.
# Use blank lines in functions, sparingly, to indicate logical sections.

# Don't put spaces around list indexes, function calls, or keyword argument assignments.

# ******** Part 3 - Naming conventions **************************

# function_name, variable_name, attribute_name
# _protected_instance_attribute
# __private_instance_attribute
# ClassName, ExceptionName
# MODULE_CONSTANTS
# (self, ...) instance methods in a class
# (cls, ...) class methods


# -*- Expression -*-
# Good: if not a_list   Bad: len(a_list) == 0
# Avoid single line if, for, while, except
# import on top of the file
#!/usr/bin/env python3  =>  in case user didn't install python3 in the default /usr/bin

# There meaningless lines are here to prevent PyCharm from warning about
# unused imports and such. We want to see real warnings only. In a
# legitimate app, those other warnings would be useful but not here.
s = sys
o = os
m = multiprocessing
z = path
z = chmod
z = chown
m = mean
c = collections
