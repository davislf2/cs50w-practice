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


print(some_method(0, 0.0))

text = "This is a string which is longer than 79 characters. This is not encouraged but will execute and run OK. Maybe."

# blank lines
# Surround top-level function and class definitions with two blank lines.
# Method definitions inside a class are surrounded by a single blank line.
# Use blank lines in functions, sparingly, to indicate logical sections.
