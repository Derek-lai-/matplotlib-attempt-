from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cbook
iterable = cbook.iterable

def assert_errors_equal(x,y,z,xerr,yerr,zerr,err):
	'''
	Assert that the error bars returned by the error bar function is
	equal to the values they should be
	'''
	if xerr is not None:
		if not iterable(xerr):
			xerr=[xerr]*len(x)

		xlines=err[2][0]._segments3d
		for i, line in enumerate(xlines):
			assert(all(line[0] == [x[i]-xerr[i], y[i], z[i]]))
			assert(all(line[1] == [x[i]+xerr[i], y[i], z[i]]))

	if yerr is not None:
		if not iterable(yerr):
			yerr=[yerr]*len(y)

		ylines=err[2][1]._segments3d
		for i,line in enumerate(ylines):
			assert(all(line[0] == [x[i], y[i]-yerr[i], z[i]]))
			assert(all(line[1] == [x[i], y[i]+yerr[i], z[i]]))

	if zerr is not None:
		if not iterable(zerr):
			zerr=[zerr]*len(z)

		zlines=err[2][2]._segments3d
		for i, line in enumerate(zlines):
			assert(all(line[0] == [x[i], y[i], z[i]-zerr[i]]))
			assert(all(line[1] == [x[i], y[i], z[i]+zerr[i]]))

def test_errorbar_zerr_none():
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')

	xs = np.arange(20)
	ys = np.arange(20)
	zs = np.arange(20)
	zerr = None
	xerr = 1
	yerr = 1
	
	err = ax.errorbar(xs,ys,zs,xerr=xerr,yerr=yerr,zerr=zerr,errorevery=1)
	assert_errors_equal(xs,ys,zs,xerr,yerr,zerr,err)

'''
if zerr is not none
	if iterable(zerr) and len(zerr) = 2 and iterable(zerr[0]) and iterable(zerr[1])
	if capsize > 0
		if lolims.any()
		if uplims.any()
'''

if __name__ == '__main__':
    import nose
    test_errorbar_zerr_none()