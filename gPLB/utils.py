## imports
#import numpy as np
#import matplotlib

### Functions

##
def as_tuple(L: list) -> tuple:
    "convert a list into a tuple"
    #return (*L,)
    return tuple(L)

##
def make_simplest_list (A: list, B: list):
    "takes a pair of list and returns a unification of them without reduplication"
    C = [ ]
    for a in A:
        if len(a) > 0 and a not in C:
            C.append(a)
    for b in B:
        if len(b) > 0 and not b in C:
            C.append (b)
    return C

##
def wrapped_make_simplest_list (*args):
    return functools.reduce(make_simplest_list, args)


### end of file
