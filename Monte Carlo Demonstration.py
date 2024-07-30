import matplotlib.pyplot as plt
import numpy as np
# from jupyterthemes import jtplot
import astropy.io.fits as pf
from scipy.optimize import curve_fit

def monte_carlo(nTrials,xparams,yparams,fnt,guess):
    fit_params = np.array([])
    xtrial = np.random.uniform(np.amin(xparams),np.amax(xparams),np.size(xparams))
    ytrial = np.random.uniform(np.amin(yparams),np.amax(yparams),np.size(yparams))
    for iTrial in range(nTrials):
        try:
            popt,pcov = curve_fit(fnt,xparams,yparams,guess)
        except:
            dummy = 1
            continue
        if np.size(fit_params) < 1:
            fit_params = np.copy(popt)
        else:
            fit_params = np.vstack((fit_params,popt))
    if len(fit_params) < 0.99*nTrials:
        print('Less than 99% of cases are well-fitted.')
        return fit_params
    else:
        return fit_params

def f_decay(x,a,b):
    return a*x**(b)
testx = np.random.uniform(0.1,5,10)
testy = 1.5/testx + np.random.normal(scale = 0.1, size = np.size(testx))
plt.errorbar(testx,testy,yerr=0.1,lw=0,elinewidth=1,ecolor='r', fmt='ko',markersize=2)

single_fit, cov = curve_fit(f_decay,testx,testy,[0,0])

x_fine = np.arange(0.1,5,0.005)
plt.errorbar(testx,testy,yerr=0.1,lw=0,elinewidth=1,ecolor='r', fmt='ko',markersize=2)
plt.plot(x_fine,f_decay(x_fine,*single_fit),ls = 'dashed',label = 'Single Fit',color='lightsteelblue') 
plt.plot(x_fine,1.5/x_fine,color='w',label = 'Theoretical Value')
plt.plot(x_fine,f_decay(x_fine,np.median(test_fit[:,0]),np.median(test_fit[:,1])),color='green',label = 'MC Fit',alpha=0.7)
plt.ylim(0,2.0);
plt.legend();

