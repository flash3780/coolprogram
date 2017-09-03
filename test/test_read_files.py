#!/usr/bin/env python

from coolprogram import *
import os

def locations():
    """Locations where test files could be found."""
    locations = ['./test_files',
                 './test/test_files',
                 '../test/test_files',
                ]
    return(locations)

def find_file(filename):
    """ Finds a file to use in tests """
    for location in locations():
        filepath = os.path.join(location, filename)
        if os.path.exists(filepath):
            return(filepath)
    raise IOError('Could not find test file.')
        
def test_read_favorite_color():
    """
    Test that favorite color is read properly

    """
    filename = 'favorite_color.csv'
    test_file = find_file(filename)

    data = read_favorite_color(test_file)
    assert( data['first_name'][1] == 'King' )
    assert( data['last_name'][1] == 'Arthur' )
    assert( data['correct_answers'][1] == 3 )
    assert( data['cross_bridge'][1] == True )
    assert( data['favorite_color'][1] == 'green' )
