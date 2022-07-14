import numpy as np
import matplotlib.pyplot as plt
from FetchData import stockdata


def normaldist(array):
    array=np.sort(array)
    
    def trasform(x, mean=None, sd=None):
        if mean == None:
            mean = np.mean(array)
        if sd == None:
            sd = np.std(array)
        return (1/(sd*np.sqrt(2*np.pi)))*np.e**((-1/2)*((x-mean)/sd)**2)
    
    f = [normald(n, np.mean(array), np.std(array)) for n in array]
    return f, plt.plot(f)