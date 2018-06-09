#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lets remember how to call callables:
"""

def eater(*positional, **named):
    """
    I talk about what I've eaten
    
    :param tuple: \*positional
    :param dict: \*\*named
    """
    print("My positional arguments, in left to right order were:")
    for idx, param in enumerate(positional):
        print("{}:  {}".format(idx, param))
        
    print("My named arguments, in no particular order were:")
    for k,v in named.items():
        if type(v) is str:
            print("{key} = '{value}'".format(key=k, value=v))            
        else:
            print("{key} = {value}".format(key=k, value=v))

# ignore when importing
if __name__ == "__main__":
    iterable_object = ["monkey", "owl", "zebra", "piranah"]
    random_dict = {"epoch": "ice age", "era" : "antebellum"}
    
    # employ both exploders
    eater(*iterable_object, **random_dict)
