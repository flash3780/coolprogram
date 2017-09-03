#!/usr/bin/env python
# -*- coding: utf-8 -*-

from coolprogram import *
import os


def test_file_locations():
    """Possible locations where test data could be found."""

    return(['./test_files',
            './tests/test_files',
            ])


def find_file(filename):
    """ Searches for a data file to use in tests """

    for location in test_file_locations():
        filepath = os.path.join(location, filename)
        if os.path.exists(filepath):
            return(filepath)
    raise IOError('Could not find test file.')


def test_read_favorite_color():
    """ Test that favorite color is read properly """

    filename = 'favorite_color.csv'
    test_file = find_file(filename)

    data = read_favorite_color(test_file)
    assert(data['first_name'][1] == 'King')
    assert(data['last_name'][1] == 'Arthur')
    assert(data['correct_answers'][1] == 3)
    assert(data['cross_bridge'][1] == True)
    assert(data['favorite_color'][1] == 'green')
