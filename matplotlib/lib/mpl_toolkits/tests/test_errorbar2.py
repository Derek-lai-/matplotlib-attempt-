from mpl_toolkits.mplot3d import Axes3D, axes3d
from matplotlib import cm
# from matplotlib.testing.decorators import image_comparison
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cbook
iterable = cbook.iterable

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

def print_value(err, header):
    print header
    i = 0
    for capline in err[1]:
        verts = capline._verts3d
        print '[',
        # print value[i]
        for vert in zip(verts):
            print str(list(vert)) + ',',
            #assert(list(vert) == val)
        print '],'
        i += 1


def assert_capline_value(err, value):
    #plotted = err[0]
    #caplines = err[1]
    #errorbarContainers = err[2]

    i = 0
    for capline in err[1]:
        verts = capline._verts3d
        print '[',
        # print value[i]
        for vert, val in zip(verts, value[i]):
            print str(list(vert)) + ',',
            assert(list(vert) == val)
        print '],'
        i += 1


    print '---'

def assert_barline_value(err, value):
    for errorbarCont, i in zip(err[2], xrange(2)):
        errorbars = errorbarCont._segments3d
        for errorbar in errorbars:
            print errorbar
            assert(errorbar == value)
    print '==='

def test_elinewidth(linewidth=None):
    X = [1, 2, 3]
    Y = [2, 1, 1]
    Z = [3, 4, 5]

    xerr = 0.3
    yerr = 0.25
    zerr = 0.5

    # elinewidth = None
    err = ax.errorbar(X, Y, Z, xerr=xerr, yerr=yerr, zerr=zerr, fmt=None)
    value = [
                [ [0.7, 1.7, 2.7], [2, 1, 1], [3, 4, 5], ],
                [ [1.3, 2.3, 3.3], [2, 1, 1], [3, 4, 5] ],
                [ [1, 2, 3], [1.75, 0.75, 0.75], [3, 4, 5] ],
                [ [1, 2, 3], [2.25, 1.25, 1.25], [3, 4, 5] ],
                [ [1, 2, 3], [2, 1, 1], [2.5, 3.5, 4.5] ],
                [ [1, 2, 3], [2, 1, 1], [3.5, 4.5, 5.5] ],
         ]
    print_value(err, 'elinewidth = None')
    assert_capline_value(err, value);

    # elinewidth != None
    err = ax.errorbar(X, Y, Z, xerr=xerr, yerr=yerr, zerr=zerr, fmt=None,
                      elinewidth=1)
    print_value(err, 'elinewidth != None')
    value = [
        [ [ 0.7,  1.7,  2.7], [2, 1, 1], [3, 4, 5], ],
        [ [ 1.3,  2.3,  3.3], [2, 1, 1], [3, 4, 5], ],
        [ [1, 2, 3], [1.75, 0.75, 0.75], [3, 4, 5] ],
        [ [1, 2, 3], [2.25, 1.25, 1.25], [3, 4, 5] ],
        [ [1, 2, 3], [2, 1, 1], [2.5, 3.5, 4.5] ],
        [ [1, 2, 3], [2, 1, 1], [3.5, 4.5, 5.5] ],
        ]
    assert_capline_value(err, value);

def test_linewidth():
    X = [1, 2, 3]
    Y = [2, 1, 1]
    Z = [3, 4, 5]

    xerr = 0.3
    yerr = 0.25
    zerr = 0.5


def test_lw():
    X = [1, 2, 3]
    Y = [2, 1, 1]
    Z = [3, 4, 5]

    xerr = 0.3
    yerr = 0.25
    zerr = 0.5


def test_transform():
    X = [1, 2, 3]
    Y = [2, 1, 1]
    Z = [3, 4, 5]

    xerr = 0.3
    yerr = 0.25
    zerr = 0.5


def test_alpha():
    X = [1, 2, 3]
    Y = [2, 1, 1]
    Z = [3, 4, 5]

    xerr = 0.3
    yerr = 0.25
    zerr = 0.5


def test_zorder():
    X = [1, 2, 3]
    Y = [2, 1, 1]
    Z = [3, 4, 5]

    xerr = 0.3
    yerr = 0.25
    zerr = 0.5


def test_iter_lolims():
    X = [1, 2, 3]
    Y = [2, 1, 1]
    Z = [3, 4, 5]

    xerr = 0.3
    yerr = 0.25
    zerr = 0.5


def test_iter_uplims():
    X = [1, 2, 3]
    Y = [2, 1, 1]
    Z = [3, 4, 5]

    xerr = 0.3
    yerr = 0.25
    zerr = 0.5


def test_iter_xlolims():
    X = [1, 2, 3]
    Y = [2, 1, 1]
    Z = [3, 4, 5]

    xerr = 0.3
    yerr = 0.25
    zerr = 0.5


def test_iter_xuplims():
    X = [1, 2, 3]
    Y = [2, 1, 1]
    Z = [3, 4, 5]

    xerr = 0.3
    yerr = 0.25
    zerr = 0.5


def test_capsize():
    X = [1, 2, 3]
    Y = [2, 1, 1]
    Z = [3, 4, 5]

    xerr = 0.3
    yerr = 0.25
    zerr = 0.5

    # capsize = 3
    err = ax.errorbar(X, Y, Z, xerr=xerr, yerr=yerr, zerr=zerr, fmt=None)
    value = [
                [ [0.7, 1.7, 2.7], [2, 1, 1], [3, 4, 5], ],
                [ [1.3, 2.3, 3.3], [2, 1, 1], [3, 4, 5] ],
                [ [1, 2, 3], [1.75, 0.75, 0.75], [3, 4, 5] ],
                [ [1, 2, 3], [2.25, 1.25, 1.25], [3, 4, 5] ],
                [ [1, 2, 3], [2, 1, 1], [2.5, 3.5, 4.5] ],
                [ [1, 2, 3], [2, 1, 1], [3.5, 4.5, 5.5] ],
         ]
    assert_capline_value(err, value);

def test_errorbar2():
    test_elinewidth()
    test_linewidth()
    test_lw()
    test_transform()
    test_alpha()
    test_zorder()
    test_iter_lolims()
    test_iter_uplims()
    test_iter_xlolims()
    test_iter_xuplims()
    test_capsize()
        


if __name__ == '__main__':
    import nose
    test_errorbar2()
