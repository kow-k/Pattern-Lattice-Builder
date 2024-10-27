### Functions

##
def as_tuple (L: list) -> tuple:
    "convert a list into a tuple"
    #return (*L,)
    return tuple(L)

##
def as_label (T: tuple, sep: str = "", add_sep_at_end: bool = False) -> str:
    "convert a given tuple to a string by concatenating its elements"
    result = ""
    if add_sep_at_end:
        for x in T:
            result += f"{x}{sep}"
    else:
        for i, x in enumerate(T):
            if i < len(T) - 1:
                result += f"{x}{sep}"
            else:
                result += f"{x}"
    #
    return result

##
def simplify_list (A: list) -> list:
    C = []
    return [ x for x in A if x is not None and x not in C ]

##
def make_simplest_list (A: list, B: list) -> list:
    "takes a list or a pair of lists and returns a unification of them without reduplication"
    C = [ ]
    for a in A:
        if len(a) > 0 and a not in C:
            C.append(a)
    for b in B:
        if len(b) > 0 and not b in C:
            C.append (b)
    return C

make_list_simplest = make_simplest_list

##
def wrapped_make_simplest_list (*args):
    import functools
    return functools.reduce(make_simplest_list, args)

## parallel filter, or pfilter
from multiprocessing import Pool
import os
cores = max(os.cpu_count(), 1)
def pfilter (func, X, cores):
    with Pool (cores) as p:
        booleans = p.map (func, X)
        return [ x for x, b in zip (X, booleans) if b ]

### end of file
