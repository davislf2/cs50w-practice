#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This is the example module. This module reference from
https://github.com/mikeckennedy/write-pythonic-code-demos/tree/master/code/ch_02_foundations
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


"""
01 - Truthiness of an element
"""


def truthiness():

    def print_truthiness(msg, exp):
        print(("TRUE" if exp else "FALSE") + " <-- " + msg)


    print_truthiness("Testing True", True)
    print_truthiness("Testing False", False)
    # for sequences

    seq = []
    print_truthiness("Empty list", seq)
    seq.append("The cat")
    print_truthiness("1 item list", seq)

    # for objects and numbers
    print_truthiness("Zero", 0)
    print_truthiness("Eleven", 11)
    print_truthiness("-Eleven", -11)

    # for None
    print_truthiness("For none", None)


    # custom types
    class AClass:
        def __init__(self):
            self.data = []

        def add(self, item):
            self.data.append(item)

        def __bool__(self):
            return True if self.data else False


    a = AClass()

    print_truthiness("Empty AClass", a)
    a.add("Thing")
    print_truthiness("nonempty AClass", a)


"""
02 - Noneness
"""

def noneness():
    # If you put db_search and db_is_available to below find_accounts, then it won't work

    db_is_available = True

    def db_search(search_text):
        return [1, 11]

    def find_accounts(search_text):
        # perform search...
        if not db_is_available:
            return None

        # returns a list of account IDs
        return db_search(search_text)


    accounts = find_accounts('python')
    if accounts is None:
        print("Error: DB not available")
    else:
        print("Accounts found: Would list them here...")


"""
03 - Multiple Compares
"""

import datetime
from enum import Enum


def multiple_compares():
    d_text = "n"
    # d_text = input("Which direction [n,s,w,e,nw,ne,sw,se]? ")
    m = Moves.parse(d_text)

    if m is None:
        print("That's not a move!")
        return

    print(m)

    # ******** less pythonic ********
    # if m == Moves.North or m == Moves.South or m == Moves.West or m == Moves.East:
    #     print("That's a direct move.")
    # else:
    #     print("That's a diagonal move.")

    # ******** more pythonic: in a set ********
    if m in {Moves.North, Moves.South, Moves.West, Moves.East}:
        print("That's a direct move.")
    else:
        print("That's a diagonal move.")

        direct_moves = {Moves.North, Moves.South, Moves.West, Moves.East}
        t0 = datetime.datetime.now()

        # speed test by davislf2
        # speed: .9 sec for multiple compare
        #        .45 sec for in a set variable (cached)
        #        2.8 sec for in a set (every time you have to initiate the set)
        for _ in range(0, 1000000):
            # b = m == Moves.North or m == Moves.South or m == Moves.West or m == Moves.East
            b = m in direct_moves
            # b = m in {Moves.North, Moves.South, Moves.West, Moves.East}
        t1 = datetime.datetime.now()
        dt = t1 - t0
        print("Time delta: {:,} sec".format(dt.total_seconds()))


class Moves(Enum):
    West = 1
    North = 2
    East = 3
    South = 4
    NorthEast = 5
    SouthEast = 6
    NorthWest = 7
    SouthWest = 8

# TODO: search @staticmethod
    @staticmethod
    def parse(text: str):
        if not text:
            return None

        text = text.strip().lower()
        if text == 'w':
            return Moves.West
        if text == 'e':
            return Moves.East
        if text == 's':
            return Moves.South
        if text == 'n':
            return Moves.North

        if text == 'nw':
            return Moves.NorthWest
        if text == 'sw':
            return Moves.SouthWest
        if text == 'ne':
            return Moves.NorthEast
        if text == 'se':
            return Moves.SouthEast

        return None


"""
04 - Randomness
"""

import random

def randomness():
    letters = "abcdefghijklmnopqrstuvwxyz1234567890"

    # BAD: C-style
    index = random.randint(0, len(letters)-1)
    item = letters[index]
    print(item)

    # Pythonic version
    item = random.choice(letters)
    print(item)

"""
05 - Stringfication
"""

def stringfication():
    name = 'Michael'
    age = 43

    # Create the string "Hi, I'm Michael and I'm 43 years old."

    # crash: print("Hi, I'm " + name + " and I'm " + age + " years old.")

    # works, but not pythonic
    # print("Hi, I'm " + name + " and I'm " + str(age) + " years old.")

    # probably pythonic
    # print("Hi, I'm %s and I'm %d years old." % (name, age))

    # pythonic
    print("Hi, I'm {} and I'm {} years old.".format(name, age))
    print("Hi, I'm {1} years old and my name is {0}, yeah {1}.".format(name, age))

    data = {'day': 'Saturday', 'office': 'Home office', 'other': 'UNUSED'}
    # print: On Saturday I was working in my Home office!
    print("On {day} I was working in my {office}!".format(**data))

    # In Python 3.6
    print("Hi, I'm {name} and I'm {age} years old.".format(name=name, age=age))
    print(f"Hi, I'm {name} and I'm {age} years old.")

"""
06 - State your state
"""

import time
import sys

# TODO: I am not sure what's the purpose of this
def state_your_state():
    confirm = input("Are you sure you want to format drive C: [yes, NO]? ")
    if not confirm or confirm.lower() != 'yes':
        print("Format cancelled!")
        sys.exit(1)

    for _ in range(40):
        time.sleep(.05)
        print('.', end='')
        sys.stdout.flush()
    print()
    print("Format completed successful. Enjoy the new hard drive space.")


"""
07 - Flat is better than nest
"""


# noinspection PyProtectedMember
import flat_support_file as s


def flat_is_better():
    download_flat()
    download_nested()
    s.download_file()

def download_flat():
    t0 = datetime.datetime.now()
    print("Let's try to download a file")
    if not s.check_download_url():
        print("Bad url")
        return

    if not s.check_network():
        print("No network")
        return

    if not s.check_dns():
        print("No DNS")
        return

    if not s.check_access_allowed():
        print("No access")
        return

    t1 = datetime.datetime.now()
    dt = t1 - t0
    print("Sweet, we can download ...")
    print("Time delta: {:,} sec".format(dt.total_seconds()))


def download_nested():
    t0 = datetime.datetime.now()
    print("Let's try to download a file")
    if s.check_download_url():
        if s.check_network():
            if s.check_dns():
                if s.check_access_allowed():
                    t1 = datetime.datetime.now()
                    dt = t1 - t0
                    print("Sweet, we can download ...")
                    print("Time delta: {:,} sec".format(dt.total_seconds()))
                else:
                    print("No access")
            else:
                print("No DNS")
        else:
            print("No network")
    else:
        print("Bad url")


if __name__ == '__main__':
    # truthiness() # 01
    # noneness() # 02
    # multiple_compares() # 03
    # randomness() # 04
    # stringfication() # 05
    # state_your_state() # 06
    flat_is_better() # 07
