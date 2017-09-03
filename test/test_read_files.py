#!/usr/bin/env python

from coolprogram import *

def test_read_favorite_color():
    """
    Test that favorite color is read properly

    """
    data = read_favorite_color('./test/test_files/favorite_color.csv')
    assert( data['correct_answers'][0] == 0 )
    assert( data['cross_bridge'][0] == False )
