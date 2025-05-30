# The Computer Language Benchmarks Game
# https://salsa.debian.org/benchmarksgame-team/benchmarksgame/
#
# contributed by Antoine Pitrou
# modified by Dominique Wahli and Daniel Nanz
# modified by Joerg Baumann
# modified by Jonathan Ultis

import sys
import multiprocessing as mp

def make_tree(dd):
    if dd == 0: #modified code: added additional check for if dd is 0
        return (None,None)
    elif dd > 0:
        return (make_tree(dd-1), make_tree(dd-1))
    return (None, None)

def check_tree(node):
    l, r = node
    if l is None:
        return 1
    else:
        return 1 + check_tree(l) + check_tree(r)

def make_check(dd, make=make_tree, check=check_tree):
    return check(make(dd))
def get_stretch_depth(stretch_depth):
    return stretch_depth

def main(n, min_depth=4):

    max_depth = max(min_depth + 2, n)
    stretch_depth = max_depth + 1

    if mp.cpu_count() > 1:
        pool = mp.Pool()
        chunkmap = pool.map
    else:
        chunkmap = map

    print('stretch tree of depth {0}\t check: {1}'.format(
          stretch_depth, make_check(stretch_depth)))

    long_lived_tree = make_tree(max_depth)

    mmd = max_depth + min_depth

    dd = min_depth
    while dd < get_stretch_depth(stretch_depth): #modified code: replace for loop with while loop including loop invariance
        ii = 2 ** (mmd - dd)
        cs = sum(chunkmap(make_check, (dd,)*ii))
        print('{0}\t trees of depth {1}\t check: {2}'.format(ii, dd, cs))
        dd = dd + 2

    print('long lived tree of depth {0}\t check: {1}'.format(
          max_depth, check_tree(long_lived_tree)))


if __name__ == '__main__':
    mp.freeze_support() #needed to be added to prevent program going into an infinite loop when converted to a .exe
    main(10) #changed from a command line argument to a literal to match the Rust and F# implementations (which also makes running the tests simpler). Ten is the argument because the Rust program was tested with a depth of ten.