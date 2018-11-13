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

def check_network():
    return True


def check_download_url():
    return True


def check_access_allowed():
    return True


def check_dns():
    return True


def download_file():
    if not check_network():
        raise ConnectionResetError("Cannot connect to network")
    if not check_download_url():
        raise ValueError("Invalid URL")
    if not check_access_allowed():
        raise PermissionError("Cannot access resource (permission denied)")
    if not check_dns():
        raise ConnectionError("No DNS")

    return ['c', 'o', 'o', 'l']
