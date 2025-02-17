#!/usr/bin/env python3

from string_functions import return_string, interpolate_string, interpolate_welcome

def test_return_string():
    '''in string_functions, function "return_string()" returns a variable of type str.'''
    assert type(return_string()) == str

def test_interpolate_string():
    '''in string_functions, function "interpolate_string()" takes a string and inserts it into another string.'''
    assert interpolate_string('Guido') == 'Hello, Guido!'

def test_interpolate_welcome():
    '''in string_functions, function "interpolate_welcome()" returns a welcome message with the given name'''
    assert interpolate_welcome('Guido') == 'Welcome, Guido!'
