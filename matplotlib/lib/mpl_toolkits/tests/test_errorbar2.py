from mpl_toolkits.mplot3d import Axes3D, axes3d
from matplotlib import cm
from matplotlib.testing.decorators import image_comparison
import matplotlib.pyplot as plt
import numpy as np


def test_errorbar2():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    X, Y, Z = axes3d.get_test_data(0.05)
    eb = ax.errorbar(X, Y, Z, xerr=1, yerr=1, zerr=5, errorevery=200,
                     capsize=10, ecolor='r')
    print eb

if __name__ == '__main__':
    import nose
    test_errorbar2()
