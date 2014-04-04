from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cbook
iterable = cbook.iterable

def setup():
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')

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

@raise(ValueError)
def test_errorbar2_errorevery1():
    """Errorevery = -2 """
    setup()
    xs = np.arange(20)
	ys = np.arange(20)
	zs = np.arange(20)
	zerr = 1
	xerr = 1
	yerr = 1
	errorevery = -2

    err = ax.errorbar(xs, ys, zs, xerr=xerr, yerr=yerr, zerr=zerr, errorevery=errorevery)
    assert_errors_equal(xs,ys,zs,xerr,yerr,zerr,err)
    
def test_errorbar2_errorevery2():
    """Errorevery = 2 """
    setup()
    xs = np.arange(20)
	ys = np.arange(20)
	zs = np.arange(20)
	zerr = 1
	xerr = 1
	yerr = 1
	errorevery = 2
   
    err = ax.errorbar(xs, ys, zs, xerr=xerr, yerr=yerr, zerr=zerr, errorevery=errorevery)
    assert_errors_equal(xs,ys,zs,xerr,yerr,zerr,err) 
    
def test_errobar2_iterable_false():
    """iterable(x) iterable(y) iterable(z) false"""
    setup()
    xs = 1
	ys = 1
	zs = 1
	zerr = 1
	xerr = 1
	yerr = 1
	errorevery = 1
   
    err = ax.errorbar(xs, ys, zs, xerr=xerr, yerr=yerr, zerr=zerr, errorevery=errorevery)
    assert_errors_equal(xs,ys,zs,xerr,yerr,zerr,err)  
    
def test_errobar2_iterable_true():
    """iterable(X) iterable(Y) iterable(Z) true"""
    setup()
    xs = np.arange(20)
	ys = np.arange(20)
	zs = np.arange(20)
	zerr = 1
	xerr = 1
	yerr = 1
	errorevery = 1
   
    err = ax.errorbar(xs, ys, zs, xerr=xerr, yerr=yerr, zerr=zerr, errorevery=errorevery)
    assert_errors_equal(xs,ys,zs,xerr,yerr,zerr,err)     
    
def test_errobar2_xerr_none():
    """xerr none"""
    setup()
    xs = np.arange(20)
	ys = np.arange(20)
	zs = np.arange(20)
	xerr = None
	zerr = 1
	yerr = 1
	errorevery = 1
   
    err = ax.errorbar(xs, ys, zs, xerr=xerr, yerr=yerr, zerr=zerr, errorevery=errorevery)
    assert_errors_equal(xs,ys,zs,xerr,yerr,zerr,err)   

def test_errorbar2_xerr_iterable():
	"""xerr iterable """
	setup()
    xs = np.arange(20)
	ys = np.arange(20)
	zs = np.arange(20)
	xerr = [1,2,3]
	zerr = 1
	yerr = 1
	errorevery = 1
   
    err = ax.errorbar(xs, ys, zs, xerr=xerr, yerr=yerr, zerr=zerr, errorevery=errorevery)
    assert_errors_equal(xs,ys,zs,xerr,yerr,zerr,err)

def test_errorbar2_xerr_iterable_len1():
	"""xerr iterable 
		T T T = F
		len = 2          
		iterable xerr[0]
		iterable xerr[1]
	"""
	setup()
    xs = np.arange(20)
	ys = np.arange(20)
	zs = np.arange(20)
	xerr = [[1,2,3],[4,5,6]]
	zerr = 1
	yerr = 1
	errorevery = 1
   
    err = ax.errorbar(xs, ys, zs, xerr=xerr, yerr=yerr, zerr=zerr, errorevery=errorevery)
    assert_errors_equal(xs,ys,zs,xerr,yerr,zerr,err)   

def test_errorbar2_xerr_iterable_len2():
	"""xerr iterable 
		F T F = T
		len = 2          
		iterable xerr[0]
		iterable xerr[1]
	"""
	setup()
    xs = np.arange(20)
	ys = np.arange(20)
	zs = np.arange(20)
	xerr = [[1,2,3,4,],2,3,4]
	zerr = 1
	yerr = 1
	errorevery = 1
   
    err = ax.errorbar(xs, ys, zs, xerr=xerr, yerr=yerr, zerr=zerr, errorevery=errorevery)
    assert_errors_equal(xs,ys,zs,xerr,yerr,zerr,err)  

def test_errorbar2_xerr_iterable_len3():
	"""xerr iterable 
		F F F = T
		len = 2          
		iterable xerr[0]
		iterable xerr[1]
	"""
	setup()
    xs = np.arange(20)
	ys = np.arange(20)
	zs = np.arange(20)
	xerr = [1,2,3,4]
	zerr = 1
	yerr = 1
	errorevery = 1
   
    err = ax.errorbar(xs, ys, zs, xerr=xerr, yerr=yerr, zerr=zerr, errorevery=errorevery)
    assert_errors_equal(xs,ys,zs,xerr,yerr,zerr,err)  
    
def test_errobar2_yerr_none():
    """yerr none"""
    setup()
    xs = np.arange(20)
	ys = np.arange(20)
	zs = np.arange(20)
	xerr = 1
	yerr = None
	zerr = 1
	errorevery = 1
   
    err = ax.errorbar(xs, ys, zs, xerr=xerr, yerr=yerr, zerr=zerr, errorevery=errorevery)
    assert_errors_equal(xs,ys,zs,xerr,yerr,zerr,err) 

def test_errorbar2_yerr_iterable_len1():
	"""yerr iterable 
		T T T = F
		len = 2          
		iterable yerr[0]
		iterable yerr[1]
	"""
	setup()
    xs = np.arange(20)
	ys = np.arange(20)
	zs = np.arange(20)
	xerr = 1
	zerr = 1
	yerr = [[1,2,3],[4,5,6]]
	errorevery = 1
   
    err = ax.errorbar(xs, ys, zs, xerr=xerr, yerr=yerr, zerr=zerr, errorevery=errorevery)
    assert_errors_equal(xs,ys,zs,xerr,yerr,zerr,err)   

def test_errorbar2_yerr_iterable_len2():
	"""yerr iterable 
		F T F = T
		len = 2          
		iterable yerr[0]
		iterable yerr[1]
	"""
	setup()
    xs = np.arange(20)
	ys = np.arange(20)
	zs = np.arange(20)
	xerr = 1
	zerr = 1
	yerr = [[1,2,3,4,],2,3,4]
	errorevery = 1
   
    err = ax.errorbar(xs, ys, zs, xerr=xerr, yerr=yerr, zerr=zerr, errorevery=errorevery)
    assert_errors_equal(xs,ys,zs,xerr,yerr,zerr,err)  

def test_errorbar2_yerr_iterable_len3():
	"""yerr iterable 
		F F F = T
		len = 2          
		iterable yerr[0]
		iterable yerr[1]
	"""
	setup()
    xs = np.arange(20)
	ys = np.arange(20)
	zs = np.arange(20)
	xerr = 1
	zerr = 1
	yerr = [1,2,3,4]
	errorevery = 1
   
    err = ax.errorbar(xs, ys, zs, xerr=xerr, yerr=yerr, zerr=zerr, errorevery=errorevery)
    assert_errors_equal(xs,ys,zs,xerr,yerr,zerr,err)  
    
def test_errobar2_zerr_none():
    """zerr none"""
    setup()
    xs = np.arange(20)
	ys = np.arange(20)
	zs = np.arange(20)
	xerr = 1
	yerr = 1
	zerr = None
	errorevery = 1
   
    err = ax.errorbar(xs, ys, zs, xerr=xerr, yerr=yerr, zerr=zerr, errorevery=errorevery)
    assert_errors_equal(xs,ys,zs,xerr,yerr,zerr,err) 

def test_errorbar2_zerr_iterable_len1():
	"""zerr iterable 
		T T T = F
		len = 2          
		iterable zerr[0]
		iterable zerr[1]
	"""
	setup()
    xs = np.arange(20)
	ys = np.arange(20)
	zs = np.arange(20)
	xerr = 1
	yerr = 1
	zerr = [[1,2,3],[4,5,6]]
	errorevery = 1
   
    err = ax.errorbar(xs, ys, zs, xerr=xerr, yerr=yerr, zerr=zerr, errorevery=errorevery)
    assert_errors_equal(xs,ys,zs,xerr,yerr,zerr,err)   

def test_errorbar2_yerr_iterable_len2():
	"""zerr iterable 
		F T F = T
		len = 2          
		iterable zerr[0]
		iterable zerr[1]
	"""
	setup()
    xs = np.arange(20)
	ys = np.arange(20)
	zs = np.arange(20)
	xerr = 1
	yerr = 1
	zerr = [[1,2,3,4,],2,3,4]
	errorevery = 1
   
    err = ax.errorbar(xs, ys, zs, xerr=xerr, yerr=yerr, zerr=zerr, errorevery=errorevery)
    assert_errors_equal(xs,ys,zs,xerr,yerr,zerr,err)  

def test_errorbar2_yerr_iterable_len3():
	"""zerr iterable 
		F F F = T
		len = 2          
		iterable zerr[0]
		iterable zerr[1]
	"""
	setup()
    xs = np.arange(20)
	ys = np.arange(20)
	zs = np.arange(20)
	xerr = 1
	yerr = 1
	zerr = [1,2,3,4]
	errorevery = 1
   
    err = ax.errorbar(xs, ys, zs, xerr=xerr, yerr=yerr, zerr=zerr, errorevery=errorevery)
    assert_errors_equal(xs,ys,zs,xerr,yerr,zerr,err)  

def test_errorbar2_barsabove_true():
	"""barsabove = true, fmt = none"""
    setup()
    xs = np.arange(20)
	ys = np.arange(20)
	zs = np.arange(20)
	xerr = 1
	yerr = 1
	zerr = 1
	errorevery = 1
	barsabove = True
   
    err = ax.errorbar(xs, ys, zs, xerr=xerr, yerr=yerr, zerr=zerr, errorevery=errorevery, barsabove=barsabove)
    assert_errors_equal(xs,ys,zs,xerr,yerr,zerr,err) 

def test_errorbar2_fmt_notnone():
	"""barsabove = flase, fmt = 'o'"""
    setup()
    xs = np.arange(20)
	ys = np.arange(20)
	zs = np.arange(20)
	xerr = 1
	yerr = 1
	zerr = 1
	errorevery = 1
	fmt='o'
   
    err = ax.errorbar(xs, ys, zs, xerr=xerr, yerr=yerr, zerr=zerr, errorevery=errorevery, fmt=fmt)
    assert_errors_equal(xs,ys,zs,xerr,yerr,zerr,err) 

def test_errorbar2_fmt_notnone():
	"""barsabove = True, fmt = 'o'"""
    setup()
    xs = np.arange(20)
	ys = np.arange(20)
	zs = np.arange(20)
	xerr = 1
	yerr = 1
	zerr = 1
	errorevery = 1
	barsabove = True
	fmt='o'
   
    err = ax.errorbar(xs, ys, zs, xerr=xerr, yerr=yerr, zerr=zerr, 
    	errorevery=errorevery, barsabove=barsabove fmt=fmt)
    assert_errors_equal(xs,ys,zs,xerr,yerr,zerr,err) 





if __name__ == '__main__':
    import nose
    test_errorbar_zerr_none()