from scipy import stats
import matplotlib.pyplot as plt

#simple linear regression using scipy.
def linearReg(X, Y):
    "returns the slope, Intercept, correlation coefficient, p-value, and standard error"
    A, B, r, p, se = stats.linregress(X, Y)
    def model(X):
        return A*X + B
    reg = list(map(model, X))
    
    plt.scatter(X, Y)
    plt.plot(X, reg)
    
    return plt.show(), A, B, r, p, se
