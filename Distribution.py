import numpy as np
import matplotlib.pyplot as plt
from FetchData import stockdata

#plots distribution of an array
def normaldist(array):
    array=np.sort(array)
    
    def transform(x, mean=None, sd=None):
        if mean == None:
            mean = np.mean(array)
        if sd == None:
            sd = np.std(array)
        return (1/(sd*np.sqrt(2*np.pi)))*np.e**((-1/2)*((x-mean)/sd)**2)
    
    f = [transform(n, np.mean(array), np.std(array)) for n in array]
    return f, plt.plot(f)


#computes returns and plot distribution
def returnsnormaldist(array):
    rets = pd.DataFrame(array)
    rets['Returns'] = rets.iloc[:, 0].pct_change().dropna()
    rets = rets.sort_values(by=['Returns'], ascending=True)
    
    def transform(x, mean=None, sd=None):
        return (1/(sd*np.sqrt(2*np.pi)))*np.e**((-1/2)*((x-mean)/sd)**2)
    
    f = [transform(n, np.mean(rets['Returns']), np.std(rets['Returns'])) for n in rets['Returns']]
    return f, plt.plot(f)
