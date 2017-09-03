#!/usr/bin/env python

from coolprogram import *
import os

def find_file(locations):
    for location in locations:
        if os.path.exists(location):
            return(location)
    raise IOError('Could not find test file.')
        
def test_read_favorite_color():
    """
    Test that favorite color is read properly

    """
    locations = ['./test_files/favorite_color.csv',
                 './test/test_files/favorite_color.csv',
                ]
    test_file = find_file(locations)

    data = read_favorite_color(test_file)
    assert( data['correct_answers'][0] == 0 )
    assert( data['cross_bridge'][0] == False )
